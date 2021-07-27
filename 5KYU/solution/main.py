def solution(array_a: list, array_b: list) -> float:
    if array_a == array_b:
        return 0.0
    squares_of_array_diff = [(i - j) ** 2 for i, j in zip(array_a, array_b)]
    return sum(squares_of_array_diff) / len(array_a)
    