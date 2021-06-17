def count(string: str) -> dict:
    dict_of_letter = {}
    for i in string:
        if i not in dict_of_letter:
            dict_of_letter[i] = 1
        else:
            dict_of_letter[i] += 1
    return dict_of_letter
    