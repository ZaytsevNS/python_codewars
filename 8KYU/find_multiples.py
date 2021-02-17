def find_multiples(integer: int, limit: int) -> list:
    return [i for i in range(integer, limit + 1) if i % integer == 0]