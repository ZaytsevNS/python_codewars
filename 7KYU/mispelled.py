# Solution for task: https://www.codewars.com/kata/5892595f190ca40ad0000095/

from difflib import SequenceMatcher


def mispelled(word1: str, word2: str) -> bool:
    if abs(len(word1) - len(word2)) > 1:
        return False
    else:
        if SequenceMatcher(isjunk=None, a=word1, b=word2).get_matching_blocks()[0].b > 1:
            return False
        else:
            return True
