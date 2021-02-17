def min_value(digits: list) -> int:
    """"This function returns the smallest number that could be formed from these digits, using the digits only once (ignore duplicates)."""
    my_arr = []
    for item in digits:
        if item not in my_arr:
            my_arr.append(item)
    return int(''.join(map(str, sorted(my_arr))))