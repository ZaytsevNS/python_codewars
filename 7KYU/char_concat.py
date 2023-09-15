# Solution for task: https://www.codewars.com/kata/55147ff29cd40b43c600058b/

def char_concat(word: str) -> str:
    result = str()
    for i in range(1, len(word) // 2 + 1):
        result += word[i - 1]
        result += word[len(word) - i]
        result += str(i)
    return result
    