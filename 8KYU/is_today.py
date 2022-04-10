# https://www.codewars.com/kata/563c13853b07a8f17c000022/

from datetime import datetime

def is_today(date) -> bool:
    return date.date() == datetime.today().date()