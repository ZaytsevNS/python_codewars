def square_digits(num):
    str_numbers = str(num)
    for i in str_numbers:
        my_array = [int(i) ** 2 for i in str_numbers]
        z = ''.join(map(str, my_array))
    return (int(z))