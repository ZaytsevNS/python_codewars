def abbrev_name(name: str) -> str:
    """ This function converts a name into initials. """
    my_abbrev = ''
    for i in name.split(' '):
        my_abbrev += i[0]
    return '.'.join(map(str, my_abbrev.upper()))