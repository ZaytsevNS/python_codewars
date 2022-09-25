# Solution for task: https://www.codewars.com/kata/5a87449ab1710171300000fd/

def tidyNumber(n: int) -> bool:
    str_num: str = str(n)
    return all(str_num[i] <= str_num[i + 1] for i in range(len(str_num) - 1))
    