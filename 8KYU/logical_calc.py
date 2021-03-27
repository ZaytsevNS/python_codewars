from functools import reduce


def logical_calc(array: list, op: str) -> bool:
    if op == "AND":
        return all(array)
    elif op == "OR":
        return any(array)
    elif op == "XOR":
        return reduce(lambda x, y: x ^ y, array)