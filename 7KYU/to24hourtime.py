# Solution for task: https://www.codewars.com/kata/59b0a6da44a4b7080300008a/

from datetime import datetime


def to24hourtime(hour: int, minute: int, period: str) -> str:
    time = datetime.strptime(f"{hour}:{minute} {period}", "%I:%M %p")
    return time.strftime("%H%M")
