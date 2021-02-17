def array_madness(arr1: list, arr2: list) -> bool:
    """ This function returns True if the sum of the squares of each element in arr1 is strictly greater than the sum of the cubes of each element in arr2. """
    if len(arr1) and len(arr2) >= 1:
        return True if sum([i**2 for i in arr1]) > sum([i**3 for i in arr2]) else False
    return False