def multiplication_table(size: int) -> list:
    result = []
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(i * j)
        result.append(row)
    return result
    