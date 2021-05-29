def show_sequence(n: int) -> str:
    if n < 0:
        return f'{n}<0'
    elif n == 0:
        return f'{n}=0'
    else:
        series = ''
        for i in range(n + 1):
            series += str(i) + '+'
        return f'{series[:-1]} = {sum(i for i in range(n + 1))}'
        