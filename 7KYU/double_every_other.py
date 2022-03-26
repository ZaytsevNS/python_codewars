def double_every_other(lst: list) -> list:
    lst_double: list = [j * 2 if not i % 2 else j for i, j in enumerate(lst, 1)]
    return lst_double