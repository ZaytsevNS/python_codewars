def repeats(arr: list) -> int:
    """ This function returns the sum of the numbers that occur only once. """
    no_repeats = []
    for i in sorted(arr):
        if arr.count(i) == 1:
            no_repeats.append(i)
    return (sum(no_repeats))
