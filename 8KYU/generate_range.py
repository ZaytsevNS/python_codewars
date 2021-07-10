def generate_range(min: int, max: int, step: int) -> list:
    """ This function generates a range of integers from min to max, with the step. """
    return [i for i in range(min, max + 1, step)]
    