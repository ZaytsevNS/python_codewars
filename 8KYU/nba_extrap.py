def nba_extrap(ppg, mpg) -> float:
    try:
        return round((48 * ppg) / mpg, 1)
    except ZeroDivisionError:
        return 0