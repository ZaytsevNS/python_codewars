def move_zeros(array):
    zero = 0
    new_array = []
    for i in array:
        if i == 0 and type(i) == int or type(i) == float:
            zero += 1
        else:
            new_array.append(i)
    new_array.extend([0] * zero)           
    return new_array