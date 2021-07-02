def multiplication_table(row: int, col: int) -> list:
    """ This function that accepts dimensions, of Rows x Columns, as parameters 
    in order to create a multiplication table sized according to the given dimensions. """
    multiplication_table: list = []
    for i in range(1, row + 1):
        row: list = []
        for j in range(1, col + 1):
            row.append(i * j)
        multiplication_table.append(row)
    return multiplication_table
