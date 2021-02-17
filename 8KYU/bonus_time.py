def bonus_time(salary:int, bonus:bool):
    if bonus is True:
        return ("$"+str(salary*10))
    return ("$"+str(salary))