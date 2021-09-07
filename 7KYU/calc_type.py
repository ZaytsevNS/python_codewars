from operator import add, sub, mul, truediv


def calc_type(a, b, res) -> str:
    operations: dict = {'addition': add,
                        'subtraction': sub,
                        'multiplication': mul,
                        'division': truediv
                        }
    return ', '.join([k for k, v in operations.items() if v(a, b) == res])
