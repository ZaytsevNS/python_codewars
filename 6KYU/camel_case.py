def camel_case(string):
    letter_title = string.title()
    total_string = letter_title.split()
    total_string = ''.join(total_string)
    return total_string