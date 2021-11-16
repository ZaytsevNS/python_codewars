import re


def seven_ate9(string: str) -> str:
    while '797' in string:
        string = re.sub(r'797', r'77', string)
    return string
