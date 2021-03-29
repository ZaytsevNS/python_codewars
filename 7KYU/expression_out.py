def expression_out(exp: str) -> str:
    dict_num = {1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine',
                10: 'Ten'}
    
    dict_op = {'+': 'Plus',
               '-': 'Minus',
               '*': 'Times',
               '/': 'Divided By',
               '**': 'To The Power Of',
               '=': 'Equals',
               '!=': 'Does Not Equal'}
    my_symb = [i for i in exp.split(' ')]
    if my_symb[1] not in dict_op.keys():
        return "That's not an operator!"
    return f'{dict_num.get(int(my_symb[0]))} {dict_op.get(my_symb[1])} {dict_num.get(int(my_symb[2]))}'
