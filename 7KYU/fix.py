def fix(s: str) -> str:
    """ This function capitalise the first letter of the first word of each sentence. """
    my_s = [i.capitalize() for i in s.split('. ')]
    return '. '.join(map(str, my_s))