def evaporator(content: int, evap_per_day: int, threshold: int) -> int:
    full = 100
    day = 0
    while full >= threshold:
        full -= full * (evap_per_day / 100)
        day += 1
    return day
    