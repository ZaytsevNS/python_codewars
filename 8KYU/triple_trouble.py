# Solution for task: https://www.codewars.com/kata/5704aea738428f4d30000914/

def triple_trouble(one: str, two: str, three: str) -> str:
    return ''.join(''.join(i + j + k) for i, j, k in zip(one, two, three))
