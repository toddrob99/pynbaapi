import logging
import pynbaapi

# Set up logging
logger = logging.getLogger("pynbaapi")
logger.setLevel(logging.DEBUG)
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)8s - %(name)s(%(thread)s) - %(message)s"
)
ch.setFormatter(formatter)
rootLogger.addHandler(ch)

# Initiate the NBA API object with a user-agent
nba = pynbaapi.nba.NBA(
    f"{pynbaapi.constants.APP_NAME} Examples/{pynbaapi.__version__.__version__}"
)

# Get a list of basic team about all teams
# List will contain objects with attributes:
# team_city, team_id, team_name, team_slug, team_tricode
# As far as I can tell, team_tricode is the same as
# team_abbreviation in other endpoints
# NOTE: this method retrieves the full season's schedule and extracts team info
# so it is a bit slow the first time. The data is cached for subsequent calls.
all_teams_basic_info = nba.all_teams()

# Get team_id for 76ers from the list of all team basic info
# Result: 1610612755 (int)
sixers_id = next(x.team_id for x in all_teams_basic_info if x.team_tricode == "PHI")

# Alternately, find the team based on abbreviation/tricode, city, or name
# and get the id from there
# Result: 1610612755 (int)
sixers_id = nba.find_team("PHI")[0].team_id

# Get more details about the team
# Response will be an object with the following data attributes:
# available_seasons: list of seasons the team has played - these have an extra
#   character prefixed on them and I'm not sure what it means
# team_info: wins, losses, division/conf name and rank, etc.
# team_season_ranks: values per game and league ranks for ast, pts, reb, opp_pts
sixers_details = nba.team(sixers_id)

# Get history about the team
# Response will be an object with the following data attributes:
# awards_championships/conf/div: list of years the team won
# background: basic info about the team including arena, dleague affiliation,
#   GM, owner, head coach, and year founded
# history: list of city/names the team has had
# hof_players, retired numbers, social_sites: self-explanatory lists
sixers_history = nba.team_history(sixers_id)

# Get the Sixers schedule for the 2021 season,
# get the details of the game on 10/20/2021,
# and extract the opponent name
sixers_schedule = nba.schedule(season="2021", team_id=sixers_id)
sixers_game_102021 = next(
    x.games[0]
    for x in sixers_schedule.league_schedule.game_dates
    if x.game_date.startswith("10/20/2021")
)
sixers_opponent_102021 = (
    sixers_game_102021.away_team.team_name
    if sixers_game_102021.away_team.team_id != sixers_id
    else sixers_game_102021.home_team.team_name
)

# Get a scoreboard of games from 10/24/2021
# Response will be an object with a scoreboard attribute
# containing a list of game objects (scoreboard.scoreboard.games)
# Each game object contains attributes such as game_id, game_time_utc,
# game_status, period, away_team & home_team (team objects), and team_leaders
scoreboard = nba.scoreboard(game_date="2021-10-24")

# Find the Sixers game in the scoreboard,
# extract the status and the final score
sixers_game = next(
    x
    for x in scoreboard.scoreboard.games
    if sixers_id in [x.away_team.team_id, x.home_team.team_id]
)
sixers_game_status = sixers_game.game_status_text
sixers_game_final_score = f"{sixers_game.away_team.team_name} ({sixers_game.away_team.score}) @ ({sixers_game.home_team.score}) {sixers_game.home_team.team_name}"

# Get the boxscore summary from the Sixers game on 10/24/21
# and get the attendance
sixers_game_box = nba.boxscore(sixers_game.game_id)
sixers_game_attendance = sixers_game_box.box_score_summary.attendance

# Get the play-by-play data for the Sixers game on 10/24/21
# and get the total count of fouls for each team
sixers_game_pbp = nba.play_by_play(sixers_game.game_id)
sixers_game_sixers_fouls = sum(
    1
    for x in sixers_game_pbp.game.actions
    if x.action_type == "Foul" and x.team_tricode == "PHI"
)
sixers_game_thunder_fouls = sum(
    1
    for x in sixers_game_pbp.game.actions
    if x.action_type == "Foul" and x.team_tricode == "OKC"
)
