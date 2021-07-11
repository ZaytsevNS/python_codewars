import random


def generate_color_rgb() -> str:
    """ This function returns randomly generated hexadecimal color string. """
    letter_and_digit = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', \
                        *[str(i) for i in range(10)]]
    color_string = '#'
    while len(color_string) < 7:
        color_string += random.choice(letter_and_digit)
    return color_string