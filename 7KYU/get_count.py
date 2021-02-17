def get_count(input_str:str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    myStr = []
    for el in input_str:
        if el in vowel:
            myStr.append(el)
    return len(myStr)