def sum_of_digits(digits) -> str: 
    if not str(digits).isdecimal():
        return ''
    else:
        return f'{" + ".join([i for i in str(digits)])} = {sum([int(i) for i in str(digits)])}'
    