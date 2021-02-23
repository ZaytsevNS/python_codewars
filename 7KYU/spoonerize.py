def spoonerize(words: str) -> str:
    """
    This function returns a spoonerism: it's a spoken phrase 
    in which the first letters of two of the words are swapped around.
    """
    if len(words.split()) == 2:
        return words.split()[1][0] + words.split()[0][1:] + ' ' + words.split()[0][0] + words.split()[1][1:]
    elif len(words.split()) == 3:
        return words.split()[2][0] + words.split()[0][1:] + ' ' + words.split()[1] + ' ' + words.split()[0][1] + words.split()[2][1:]
    else:
        return words

