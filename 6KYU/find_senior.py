def find_senior(lst: list) -> list: 
    return ([i for i in lst if i['age'] == max([i['age'] for i in lst])])
