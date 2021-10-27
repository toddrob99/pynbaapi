from pynbaapi.nba import NBA


class TestTeams():
    def test_team_by_id(self):
        nba = NBA()
        sixers = nba.team(1610612755)
        assert sixers.team_info.team_id == 1610612755
        assert sixers.team_info.team_city == "Philadelphia"
        assert sixers.team_info.team_name == "76ers"
        assert sixers.team_info.team_abbreviation == "PHI"

    def test_all_teams(self):
        nba = NBA()
        all_teams = nba.all_teams(force_refresh=True)
        assert len(all_teams) == 30
        for team in all_teams:
            assert isinstance(team.team_id, int)
            assert isinstance(team.team_city, str)
            assert isinstance(team.team_name, str)
            assert isinstance(team.team_tricode, str)
            assert len(team.team_tricode) == 3

    def test_find_team_by_abbreviation(self):
        nba = NBA()
        matching_teams = nba.find_team("BKN")
        assert len(matching_teams) == 1
        nets = matching_teams[0]
        assert nets.team_id == 1610612751
        assert nets.team_city == "Brooklyn"
        assert nets.team_name == "Nets"
        assert nets.team_tricode == "BKN"

    def test_find_team_by_city(self):
        nba = NBA()
        matching_teams = nba.find_team("Toronto")
        assert len(matching_teams) == 1
        raptors = matching_teams[0]
        assert raptors.team_id == 1610612761
        assert raptors.team_city == "Toronto"
        assert raptors.team_name == "Raptors"
        assert raptors.team_tricode == "TOR"

    def test_team_history(self):
        nba = NBA()
        sixers_history = nba.team_history(team_id=1610612755)
        assert sixers_history.background.abbreviation == "PHI"
        assert sixers_history.background.city == "Philadelphia"
        assert sixers_history.background.nickname == "76ers"
        assert sixers_history.background.team_id == 1610612755
        assert len(sixers_history.awards_championships) >= 3
        assert sixers_history.awards_championships[0].yearawarded == 1955
        assert sixers_history.awards_championships[1].yearawarded == 1967
        assert sixers_history.awards_championships[2].yearawarded == 1983
        assert len(sixers_history.awards_conf) >= 5
        assert sixers_history.awards_conf[0].yearawarded == 1977
        assert sixers_history.awards_conf[1].yearawarded == 1980
        assert sixers_history.awards_conf[4].yearawarded == 2001
        assert len(sixers_history.awards_div) >= 12
        assert len(sixers_history.hof_players) >= 17
        assert len(sixers_history.retired_numbers) >= 10
        assert len(sixers_history.history) >= 2
        assert sixers_history.history[0].team_id == 1610612755
        assert sixers_history.history[1].team_id == 1610612755

    def test_team_roster(self):
        nba = NBA()
        sixers_2019_roster = nba.team_roster(1610612755, 2019)
        assert len(sixers_2019_roster.team_roster) == 17
        assert len(sixers_2019_roster.team_coaches) == 7
