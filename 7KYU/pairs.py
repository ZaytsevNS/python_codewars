def pairs(array: list) -> int:
    """ This function returns the count of pairs that have consecutive numbers. """
    pairs_from_array = list(zip(array[::2], array[1::2]))
    count = 0
    for i, j in pairs_from_array:
        if (i - j == 1) or (i - j == -1):
            count += 1
    return count
