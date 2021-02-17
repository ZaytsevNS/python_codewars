def remove_every_other(my_list: list) -> list:
    """ This function removes every second element from the array. """
    new_list = []
    for i, k in enumerate(range(len(my_list))):
        if i % 2 == 0:
            new_list.append(my_list[i])
    return new_list