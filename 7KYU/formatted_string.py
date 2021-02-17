def solution(c: int) -> str:
    """ This function returns a formatted string. """
    return 'Value is ' + ('0000' + str(c))[-5:]