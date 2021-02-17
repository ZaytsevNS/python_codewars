def filter_list(arr: list) -> list:
    """This function returns a new list with the strings filtered out."""
    my_list = []
    for item in arr:
        if str(item).isdigit() and type(item) != str:
            my_list.append(item)
    return my_list