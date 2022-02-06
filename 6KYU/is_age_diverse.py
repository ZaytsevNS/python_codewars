def is_age_diverse(lst: list) -> bool: 
    ages: dict = {
        'teens': [range(10, 20), 0],
        'twenties': [range(20,30), 0],
        'thirties': [range(30, 40), 0],
        'forties': [range(40, 50), 0],
        'fifties': [range(50, 60), 0],
        'sixties': [range(60, 70), 0],
        'seventies': [range(70, 80), 0],
        'eighties': [range(80, 90), 0],
        'nineties': [range(90, 100), 0],
        'centenarian': [range(100, 200), 0],
    }
    for v in ages.values():
        for i in lst:
                if i['age'] in v[0]:
                        v[1] += 1
                else: pass
    return all([i[1] for i in ages.values()])
