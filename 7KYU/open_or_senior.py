from typing import List


def open_or_senior(data: List[int]) -> List[str]:
    categories_of_membership: list = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            categories_of_membership.append('Senior')
        else:
            categories_of_membership.append('Open')
    return categories_of_membership
    