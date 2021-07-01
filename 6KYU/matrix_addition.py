from numpy import matrix


# Solution with numpy
def matrix_addition(a: list, b: list) -> list:
    """ This function accepts two square matrices (N x N two dimensional arrays), 
    and return the sum of the two. """
    return (matrix(a) + matrix(b)).tolist()

# Solution without numpy
# def matrix_addition(a: list, b: list) -> list:
#     matrix_sum: list = []
#     for i in range(len(a)):
#         row: list = []
#         for j in range(len(a[i])):
#             row.append(a[i][j] + b[i][j])
#         matrix_sum.append(row)
#     return matrix_sum
