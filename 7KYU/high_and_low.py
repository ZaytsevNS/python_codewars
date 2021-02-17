def high_and_low(string: str) -> str:
    """This function returns the highest and lowest number."""
    my_num = []
    for item in string.split():
        my_num.append(int(item))
        high = max(my_num)
        low = min(my_num)
    return ''.join(map(str, str(high)+' '+str(low)))