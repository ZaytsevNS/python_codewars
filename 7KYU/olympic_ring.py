from math import floor


def olympic_ring(string: str) -> str:
    my_dict = {
        1: ['q', 'Q', 'e', 'R', 'o', 'O', 'p', 'P', 'a', 'A', 'd', 'D', 'g', 'b'],
        2: ['B']
    }
    ring = 0
    for i in string:
        if i.isalpha():
            for key, val in my_dict.items():
                if i in val:
                    ring += key
    result = floor(ring / 2)
    if result <= 1:
        return 'Not even a medal!'
    elif result == 2:
        return 'Bronze!'
    elif result == 3:
        return 'Silver!'
    return 'Gold!'