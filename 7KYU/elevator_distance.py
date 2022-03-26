def elevator_distance(array: list) -> int:
    return sum([abs(array[i] - array[i+1]) for i in range(len(array)-1)])