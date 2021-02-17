def kebabize(string):
    myString = ''
    for letter in string:
        if not letter.isdigit():
            myString += letter
    for letter_myString in myString:
        if letter_myString.istitle():
            myString = myString.replace(letter_myString, '-' + letter_myString.lower())
    if myString.startswith('-'):
        return myString[1:]
    return myString