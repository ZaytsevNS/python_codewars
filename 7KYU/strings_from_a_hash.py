def solution(d: dict) -> str:
    my_list = []
    for key in d:
        my_list.append(f'{key} = {d[key]}')
    my_list = sorted(my_list)
    return ','.join(my_list)