def index(array: list, n: int) -> int:
    """ This function find the N-th power of the element in the array with the index N. """
    for k, i in enumerate(range(len(array))):
        if i == n:
            return (array[i] ** n)
    return -1