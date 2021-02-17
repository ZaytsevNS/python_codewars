def str_count(string: str, letter: str) -> int:
    """ This function returns an integer of the count of occurrences the 2nd argument is found in the first one. """
    count_letter = 0
    for i in string:
        if i == letter:
            count_letter += 1
    return count_letter