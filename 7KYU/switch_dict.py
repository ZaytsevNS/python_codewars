def switch_dict(d: dict):        
    new_dict: dict = {}
    for key, value in d.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(key)
    return new_dict
