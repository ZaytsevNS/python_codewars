def switch_it_up(number: int) -> str:
    ''' This function returns number (0-9) in words. '''
    dict_num = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    return dict_num.get(number)