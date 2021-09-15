import re


def uncollapse(digits: str) -> str:
    result = re.findall(r'(zero)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten)', digits)            
    return ' '.join([j for i in result for j in i if j])
