# Solution for task: https://www.codewars.com/kata/570523c146edc287a50014b1/

def number_joy(n: int) -> bool:
    digit_sum: int = sum(int(i) for i in str(n))
    return digit_sum * int(str(digit_sum)[::-1]) == n
    