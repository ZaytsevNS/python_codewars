from typing import Union


def task(w: str, n: Union[int, float], c: Union[int, float]) -> str:
    workers: dict = {
        'Monday': 'James',
        'Tuesday': 'John',
        'Wednesday': 'Robert',
        'Thursday': 'Michael',
        'Friday': 'William'
    }
    return f'It is {w} today, {workers[w]}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid'

