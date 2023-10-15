import operator


def calculator(txt: str) -> str:
    split_txt: list = txt.split()
    operations: dict = {'+': operator.add(len(split_txt[0]), len(split_txt[2])),
                        '-': operator.sub(len(split_txt[0]), len(split_txt[2])),
                        '*': operator.mul(len(split_txt[0]), len(split_txt[2])),
                        '//': operator.floordiv(len(split_txt[0]), len(split_txt[2]))}
    return operations.get(split_txt[1]) * '.'
