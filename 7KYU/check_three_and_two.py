import collections


def check_three_and_two(array: list) -> bool:
    count_letter = collections.Counter()
    for letter in array:
        count_letter[letter] += 1
    if max(count_letter.values()) == 3 and min(count_letter.values()) == 2:
        return True
    return False
    