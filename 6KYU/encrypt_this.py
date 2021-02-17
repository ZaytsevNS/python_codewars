def encrypt_this(text):
    myStr = text.split()
    for i, letter in enumerate(myStr):
        if len(letter) == 1:
            myStr[i] = str(ord(letter))
        elif len(letter) == 2:
            myStr[i] = str(ord(letter[0]))+letter[1]
        else:
            myStr[i] = str(ord(letter[0])) + letter[-1] + letter[2:-1] + letter[1]
    return ' '.join(myStr)