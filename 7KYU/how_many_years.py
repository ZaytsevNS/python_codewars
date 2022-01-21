def how_many_years(date1: str, date2: str) -> int:
    return abs(int(date1.split('/')[0]) - int(date2.split('/')[0]))
