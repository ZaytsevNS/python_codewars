def reverse_letter(string: str) -> str:
    """This function returns reversed string with alphabetic characters."""
    my_string = ''
    for item in string:
        if item.isalpha():
            my_string += item
    return ''.join(map(str, list(reversed(my_string))))
