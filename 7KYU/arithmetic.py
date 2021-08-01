def arithmetic(a, b, operator):
    op: dict = {'add': '+',
               'subtract': '-',
               'multiply': '*',
               'divide': '/'}
    return eval(f'{a}{op.get(operator)}{b}')
    