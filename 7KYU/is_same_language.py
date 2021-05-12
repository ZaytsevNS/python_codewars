from typing import List


def is_same_language(lst: List[dict]) -> bool: 
    return True if len(set([i['language'] for i in lst])) == 1 else False
    