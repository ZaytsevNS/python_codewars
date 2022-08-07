# Solution for task: https://www.codewars.com/kata/5aa20a964a6b34417c00008d/


from typing import List


def find_page_number(pages: List[int]) -> list:
    start_page: int = 1
    incorrect_pages: list = []
    for item in pages:
        if item == start_page:
            start_page += 1
        else:
            incorrect_pages.append(item)
    return incorrect_pages
