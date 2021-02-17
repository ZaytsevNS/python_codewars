def square_sum(numbers):
    """ This function returns the square sum. """
    return sum([i ** 2 for i in numbers]) if len(numbers) > 0 else 0