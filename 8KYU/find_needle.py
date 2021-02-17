def find_needle(haystack):
    for i, el in enumerate(haystack):
        if el == 'needle':
            return (f"found the needle at position {i}".format(i))