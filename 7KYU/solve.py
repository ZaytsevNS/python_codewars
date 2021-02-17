def solve(arr: list) -> int:
    """ This function returns one integer that is either only negative or only positive. """
    for i in range(len(arr)):
        if -arr[i] not in arr:
            return arr[i]