def multi_table(number: int):
    """ This function returns multiplication table for 'number'. """
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))