def odd_or_even(n:list):
    if len(n) == 0:
        return [0]
    elif sum(n) % 2 == 0:
        return "even"
    else:
        return "odd"