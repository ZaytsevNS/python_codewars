def points(games: list) -> int:
    """ This function counts the points of our team in the championship. """
    score = 0
    for item in range(len(games)):
        x = games[item][0]
        y = games[item][2]
        if x > y:
            score += 3
        elif x == y:
            score += 1
    return score