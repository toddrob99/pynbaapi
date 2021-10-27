from pynbaapi.nba import NBA


class TestGames():
    def test_schedule(self):
        nba = NBA()
        sixers_2019_schedule = nba.schedule(season=2019, team_id=1610612755)
        assert len(sixers_2019_schedule.league_schedule.game_dates) == 77
        assert sixers_2019_schedule.league_schedule.game_dates[0].game_date == "10/23/2019 12:00:00 AM"
        assert len(sixers_2019_schedule.league_schedule.game_dates[0].games) == 1
        assert sixers_2019_schedule.league_schedule.game_dates[0].games[0].game_code == "20191023/BOSPHI"
        assert sixers_2019_schedule.league_schedule.game_dates[0].games[0].game_id == "0021900008"
        assert sixers_2019_schedule.league_schedule.game_dates[0].games[0].game_status == 3
        assert sixers_2019_schedule.league_schedule.game_dates[0].games[0].game_status_text == "Final"
        assert sixers_2019_schedule.league_schedule.game_dates[0].games[0].week_number == 1

    def test_scoreboard(self):
        nba = NBA()
        scoreboard = nba.scoreboard(game_date="2021-10-25")
        pass
        assert scoreboard.scoreboard.game_date == "2021-10-25"
        assert scoreboard.scoreboard.league_id == "00"
        assert len(scoreboard.scoreboard.games) == 9
        assert scoreboard.scoreboard.games[0].game_code == "20211025/BOSCHA"
        assert scoreboard.scoreboard.games[0].game_status == 3
        assert scoreboard.scoreboard.games[0].game_status_text == "Final/OT"
        assert scoreboard.scoreboard.games[0].away_team.team_tricode == "BOS"
        assert scoreboard.scoreboard.games[0].home_team.team_tricode == "CHA"

    def test_boxscore(self):
        nba = NBA()
        box = nba.boxscore("0022100049")
        assert box.box_score_summary.attendance == 15672
        assert box.box_score_summary.game_id == "0022100049"
        assert box.box_score_summary.game_code == "20211025/PORLAC"
        assert box.box_score_summary.arena.arena_id == 137
        assert box.box_score_summary.away_team_id == 1610612757
        assert box.box_score_summary.home_team_id == 1610612746
        assert len(box.box_score_summary.last_five_meetings.meetings) == 5
        assert box.box_score_summary.period == 4
        assert box.box_score_summary.pregame_charts.away_team.statistics.points == 113.7
        assert box.box_score_summary.postgame_charts.home_team.statistics.steals == 21.0

    def test_play_by_play(self):
        nba = NBA()
        pbp = nba.play_by_play("0022100041")
        assert pbp.game.game_id == "0022100041"
        assert len(pbp.game.actions) == 568
        assert pbp.game.actions[0].action_type == "period"
        assert pbp.game.actions[0].sub_type == "start"
        assert pbp.game.actions[300].action_type == "Made Shot"
        assert pbp.game.actions[300].sub_type == "Jump Shot"
        assert pbp.game.actions[300].clock == "PT04M32.00S"
        assert pbp.game.actions[300].is_field_goal == 1
        assert pbp.game.actions[300].period == 3
        assert pbp.game.actions[300].person_id == 1629684
        assert pbp.game.actions[300].points_total == 171
        assert pbp.game.actions[300].score_away == "86"
        assert pbp.game.actions[300].score_home == "85"
        assert pbp.game.actions[300].shot_distance == 9
        assert pbp.game.actions[300].team_tricode == "BOS"
