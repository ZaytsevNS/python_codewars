# Solution for task: https://www.codewars.com/kata/554dc2b88fbafd2e95000125/

def vector_length(vector: list):
    """ This function returns the vector's length """
    return sum([(k - i)**2 for i, k in zip(vector[0], vector[1])])**0.5
