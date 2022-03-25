def unused_digits(*args) -> str:
    """ Given a list of integers, return the digits that are not present in any of them. """
    digit: set = set(''.join(map(str, [i for i in range(0, 10)])))
    digit_from_args: set = set(''.join(map(str, [i for i in args])))
    return ''.join(sorted(digit - digit_from_args))
