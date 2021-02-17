def difference_in_ages(ages: list) -> tuple:
    """ This function returns 'min', 'max' in ages and calculate the difference between them. """
    return (min(ages), max(ages), max(ages) - min(ages))