def reverse_words(x:str):
    my_revers = []
    for item in x.split(' '):
        my_revers.append(item[::-1])
    return (' '.join(map(str, my_revers)))
