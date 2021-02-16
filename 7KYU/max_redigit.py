def max_redigit(num: int) -> int:
    """ This function takes one positive three digit integer and rearranges its digits to get maximum possible number. """
    if len(str(num)) != 3 or not str(num).isdigit():
        return None
    digit = []
    for i in str(num):
        digit.append(int(i))
    return int(''.join(map(str, sorted(digit, reverse = True))))