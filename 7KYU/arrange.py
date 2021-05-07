from typing import List


def arrange(arr: List[str]) -> List[str]:
    if len(arr) < 2:
        return arr
    weight_of_grams = []
    for i in arr:
        if i.endswith('G') and not i.endswith('KG'):
            weight_of_grams.append((int(i[:-1]), i))
        elif i.endswith('KG'):
            weight_of_grams.append(((int(i[:-2]) * 1000), i))
        elif i.endswith('T'):
            weight_of_grams.append(((int(i[:-1]) * 1_000_000), i))
    return [i[1] for i in sorted(weight_of_grams)]
