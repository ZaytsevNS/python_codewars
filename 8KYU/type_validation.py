# Solution for task: https://www.codewars.com/kata/59c1302ecb7fb48757000013/


def type_validation(variable, _type) -> bool: 
    return _type in str(type(variable))
