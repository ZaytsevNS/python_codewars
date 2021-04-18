def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    return True if mpg * fuel_left >= distance_to_pump else False
    