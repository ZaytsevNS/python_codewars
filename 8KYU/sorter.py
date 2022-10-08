# Solution for task: https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/

def sorter(textbooks: list) -> list:
    return sorted(textbooks, key=str.casefold)
