from typing import List


def is_valid_walk(walk: List[str]) -> bool:
    if len(walk) != 10:
        return False
    string_of_my_walk_rout = ''.join(walk)
    if string_of_my_walk_rout.count('n') == string_of_my_walk_rout.count('s') and string_of_my_walk_rout.count('e') == string_of_my_walk_rout.count('w'):
        return True
    return False
    