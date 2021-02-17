def max_number(n: int) -> int:
    ''' This function returns the maximum number could be formed from the digits of the number given (n). '''
    my_arr = []
    for i in str(n):
        my_arr.append(int(i))
    return int(''.join(map(str, sorted(my_arr, reverse=True))))