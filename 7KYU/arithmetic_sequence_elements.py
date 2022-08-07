# Solution for task: https://www.codewars.com/kata/55caf1fd8063ddfa8e000018/


def arithmetic_sequence_elements(a, d, n) -> str:
    return ', '.join(map(str, [a + d * (i - 1) for i in range(1, n + 1)]))
    