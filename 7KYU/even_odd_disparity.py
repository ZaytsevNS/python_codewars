def solve(arr: list) -> int:
    """ This function returns the difference between the count of even numbers and the count of odd numbers. """
    even = []
    odd = []
    for item in arr:
        if str(item).isdigit():
            if item % 2 == 0:
                even.append(item)
            else:
                odd.append(item)
    return len(even) - len(odd)