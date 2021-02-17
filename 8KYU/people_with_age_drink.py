def people_with_age_drink(age: int) -> str:
    drinks = ['toddy', 'coke', 'beer', 'whisky']
    if age < 14:
        return f'drink {drinks[0]}'
    elif 14 <= age < 18:
        return f'drink {drinks[1]}'
    elif 18 <= age < 21:
        return f'drink {drinks[2]}'
    return f'drink {drinks[-1]}'