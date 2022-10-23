# Solution for task: https://www.codewars.com/kata/545991b4cbae2a5fda000158/

def include(arr: list, item: int) -> bool:
    """
    This function returns true if the item belongs to the list, otherwise false.
    """
    return bool(arr.count(item))
