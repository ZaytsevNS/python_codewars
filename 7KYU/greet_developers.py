def greet_developers(lst: list) -> list:
    for i in lst:
        i.update({'greeting': f'Hi {i["firstName"]}, what do you like the most about {i["language"]}?'})
    return lst
