def remove_smallest(numbers):
    if len(numbers) == 0:
        return ([])    
    new_list = list(numbers)
    my_min = min(new_list)
    del new_list[new_list.index(my_min)]
    return (new_list)