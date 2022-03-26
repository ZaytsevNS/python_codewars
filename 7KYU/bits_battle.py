def bits_battle(num: list) -> str:
    count_one = sum([bin(i)[2:].count('1') for i in num if i % 2])
    count_zero = sum([bin(i)[2:].count('0') for i in num if not i % 2])
    if count_one > count_zero:
        return 'odds win'
    elif count_one < count_zero:
        return 'evens win'
    else:
        return 'tie'