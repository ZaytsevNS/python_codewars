# Solution for task: https://www.codewars.com/kata/55c45be3b2079eccff00010f/

import re

def order(sentence: str) -> str:
    order_and_word: dict = {}
    for word in sentence.split():
        order = int(re.search(r'\d', word).group())
        order_and_word[order] = word
    return ' '.join([v for k, v in sorted(order_and_word.items())])
