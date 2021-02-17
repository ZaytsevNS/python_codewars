def dont_give_me_five(start: int, end: int) -> int:
    """This function returns the count of all numbers except numbers with a 5."""
    count = 0
    for item in range(start, end+1):
        if '5' not in str(item):
            #print (item)
            count += 1
    return count