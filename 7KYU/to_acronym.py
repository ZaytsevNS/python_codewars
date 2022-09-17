# Solution for task: https://www.codewars.com/kata/57a60bad72292d3e93000a5a/


def to_acronym(inp: str) -> str:
    """ This function takes a string and make an acronym of it. """
    return ''.join(i[0] for i in inp.split()).upper()
