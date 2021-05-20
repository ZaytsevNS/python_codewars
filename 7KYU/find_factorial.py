def factorial(n: int):
    if n == 0 or n == 1:
        return 1
    elif 2 <= n < 13:
        return n * factorial(n - 1)
    else:
        raise ValueError('Value Error')
        