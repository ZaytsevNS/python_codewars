def premier_league_standings(teams: dict) -> dict:
    if len(teams) < 2:
        return teams
    new_season_standings: dict = {}
    other_teams: list = []
    for k, v in teams.items():
        if k == 1:
            new_season_standings[k] = v
        else:
            other_teams.append(v)
    for idx, val in enumerate(sorted(other_teams), start=2):
        new_season_standings[idx] = val
    return new_season_standings
    