def count_developers(lst) -> int:
    return len([i for i in lst if i['continent'] == 'Europe' and i['language'] == 'JavaScript'])
    