def quarter_of(month: int) -> int:
    """ This function returns to which quarter of the year it belongs as an integer number. """
    quartal = {1: [1, 2, 3],
               2: [4, 5, 6],
               3: [7, 8, 9],
               4: [10, 11, 12]}
    for key, val in quartal.items():
        for i in val:
            if i == month:
                return key