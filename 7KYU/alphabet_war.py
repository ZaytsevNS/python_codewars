def alphabet_war(fight: str) -> str:
    power_of_letters = {"left_side": {'w': 4, 'p': 3, 'b': 2, 's': 1}, 
                        "right_side": {'m': 4, 'q': 3, 'd': 2, 'z': 1}}
    power_left = 0
    power_right = 0
    for i in fight:
        if i in power_of_letters['left_side']:
            power_left += power_of_letters['left_side'][i]
        elif i in power_of_letters['right_side']:
            power_right += power_of_letters['right_side'][i]
    if power_right > power_left:
        return 'Right side wins!'
    elif power_right == power_left:
        return 'Let\'s fight again!'
    return 'Left side wins!'