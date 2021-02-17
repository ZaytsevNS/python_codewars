import re


def solve(s: str) -> int:
    """
    This function returns the largest number from string.
    """
    num = re.findall(r'\d+', s)
    int_num = []
    for i in num:
        int_num.append(int(i))
    return max(int_num)