def is_uppercase(inp: str) -> bool:
    """ This function returns True if string is ALL CAPS else False. """
    for i in inp.split():
        if i.isupper():
            return True
        return False