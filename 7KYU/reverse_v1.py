# Solution for task: https://www.codewars.com/kata/5413759479ba273f8100003d/

def reverse(lst: list) -> list:
    empty_list: list = list()
    for i in lst:
        empty_list.insert(0, i)
    return empty_list
    