# Solution for task: https://www.codewars.com/kata/57faf7275c991027af000679/


def remove(s: str, n: int) -> str:
    """
    Remove n exclamation marks in the sentence from left to right. n is positive integer.
    """
    return s.replace('!', '', n)
