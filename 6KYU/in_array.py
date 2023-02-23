# Solution for task: https://www.codewars.com/kata/550554fd08b86f84fe000a58/

def in_array(array1: list, array2: list) -> list:
    words: list = []
    for i in array1:
        for j in array2:
            if (i in j) and (i not in words):
                words.append(i)
    return sorted(words)
