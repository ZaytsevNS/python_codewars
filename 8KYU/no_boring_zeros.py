from numpy import trim_zeros

def no_boring_zeros(num: int) -> int:
    digit_num = []
    for i in str(abs(num)):
        digit_num.append(int(i))
    if num < 0:
        return int(f'-{"".join(map(str, trim_zeros(digit_num)))}')
    elif num == 0:
        return 0
    return int("".join(map(str, trim_zeros(digit_num))))