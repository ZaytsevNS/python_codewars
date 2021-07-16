def insurance(age: int, size: str, num_of_days: int) -> int:
    """ This function returns an integer number of the calculated total cost of the rental. """ 
    if num_of_days <= 0:
        return 0
    if age < 25:
        if size == 'economy':
            return 60 * num_of_days
        elif size == 'medium':
            return 70 * num_of_days
        else:
            return 75 * num_of_days
    else:
        if size == 'economy':
            return 50 * num_of_days 
        elif size == 'medium':
            return 60 * num_of_days
        else:
            return 65 * num_of_days
        