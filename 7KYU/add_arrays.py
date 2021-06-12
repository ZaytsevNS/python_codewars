def add_arrays(array1: list, array2: list) -> list:
    if len(array1) == len(array2):
        return [i + j for i, j in zip(array1, array2)]
    raise Exception("Input arguments are not of equal length")
