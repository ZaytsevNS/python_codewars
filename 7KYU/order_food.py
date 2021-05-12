from typing import List


def order_food(lst: List[dict]) -> dict: 
    meals = {}
    for i in lst:
        if i['meal'] not in meals:
            meals[i['meal']] = 1
        else:
            meals[i['meal']] += 1
    return meals
    