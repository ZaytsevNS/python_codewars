from math import ceil


def what_century(year: str) -> str:
    """ This function returns the century of the input year. """
    century = str(ceil(int(year) / 100))
    if century[-1] == '1':
        if century == '11':
            return century + 'th'
        return century + 'st'
    if century[-1] == '2':
        if century == '12':
            return century + 'th'
        return century + 'nd'
    if century[-1] == '3':
        if century == '13':
            return century + 'th'
        return century + 'rd'
    return century + 'th'