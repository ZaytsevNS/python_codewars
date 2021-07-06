from itertools import permutations
from typing import List


def anagrams(word: str, words: List[str]) -> List[str]:
    list_of_permutations: list = list({''.join(map(str, i)) for i in set(list(permutations(word)))})
    return [i for i in words if i in list_of_permutations]
    