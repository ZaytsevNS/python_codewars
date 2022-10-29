# Solution for task: https://www.codewars.com/kata/596343a24489a8b2a00000a2/

import re


def is_it_a_num(s: str) -> str:
    num: str = ''.join(re.findall(r'\d', s))
    if len(num) == 11 and num.startswith('0'):
        return num
    else:
        return "Not a phone number"
