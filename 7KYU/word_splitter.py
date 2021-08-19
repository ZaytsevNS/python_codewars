SEPARATOR: list = [':', ',', '*', ';', '#', '|', '+', '%', '>', '?', '&', '=', '!']
def word_splitter(string: str) -> list:
    for i in string:
        if i in SEPARATOR:
            string = string.replace(i, ' ')
    return string.split()
    