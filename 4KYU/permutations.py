from itertools import permutations as pm
from typing import List


def permutations(string: str) -> List[str]:
    return sorted([''.join(i) for i in set(pm(string))])
    