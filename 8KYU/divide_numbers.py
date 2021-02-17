def divide_numbers(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Division by zero :-('