def capital(capitals): 
    list_of_capitals = []
    for i in capitals:
        for k, v in i.items():
            if k == 'state':
                list_of_capitals.append(f'The capital of {i.get("state")} is {i.get("capital")}')
            elif k == 'country':
                list_of_capitals.append(f'The capital of {i.get("country")} is {i.get("capital")}')
    return list_of_capitals
    