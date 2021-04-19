from typing import List
from math import floor


def gps(s: int, x: List[float]) -> int:
    average_hourly_speed = [3600 * (x[i + 1] - x[i]) / s for i in range(len(x) - 1)]
    return floor(max(average_hourly_speed)) if len(x) > 1 else 0
    