def boredom(staff: dict) -> str:
    dict_score = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    boredom_score = 0
    for v in staff.values():
        if v in dict_score:
            boredom_score += dict_score.get(v)
    return 'kill me now' if boredom_score <= 80 else 'i can handle this' if 80 < boredom_score < 100 else 'party time!!'
    