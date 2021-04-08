from typing import List


def paul(x: List[str]) -> str:
    dict_with_points = {
        'kata': 5,
        'Petes kata': 10,
        'life': 0,
        'eating': 1
    }
    misery_score: int = 0
    for i in x:
        if i in dict_with_points:
            misery_score += dict_with_points.get(i)
    if misery_score < 40:
        return 'Super happy!'
    elif 40 <= misery_score < 70:
        return 'Happy!'
    elif 70 <= misery_score < 100:
        return 'Sad!'
    return 'Miserable!'
    