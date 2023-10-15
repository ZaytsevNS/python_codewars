import string


def pass_the_door_man(word: str) -> int: 
    """ This function finds the doubled letter's position of the given word in the alphabet 
    and multiply this number per 3. """
    try:
        alphabet = {k:v for k, v in enumerate(string.ascii_lowercase, start=1)}
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                for k, v in alphabet.items():
                    if word[i] in v:
                        return k * 3
    except:
        return -1
    