def find_missing(sequence: list) -> int:
    d = (sequence[-1] - sequence[0]) // len(sequence)
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != d:
            return sequence[i] + d
            