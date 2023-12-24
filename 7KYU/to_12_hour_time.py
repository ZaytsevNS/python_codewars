# Solution for task: https://www.codewars.com/kata/59b0ab12cf3395ef68000081/

from datetime import datetime


def to_12_hour_time(time_string: str) -> str:
    time_string_datetime = datetime.strptime(time_string, "%H%M")
    return time_string_datetime.strftime("%-I:%M %p").lower()
