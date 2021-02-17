def even_or_odd(s: str) -> str:
    """
    Given a string of digits confirm whether the sum of all the individual
    even digits are greater than the sum of all the indiviudal odd digits.
    """
    sum_even, sum_odd = sum([int(i) for i in s if int(i) % 2 == 0]), sum([int(i) for i in s if int(i) % 2 != 0])
    if sum_even > sum_odd:
        return "Even is greater than Odd"
    elif sum_even < sum_odd:
        return "Odd is greater than Even"
    return "Even and Odd are the same"