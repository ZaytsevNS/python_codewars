def add(num1: int, num2: int) -> int:
    num1: str = str(num1)
    num2: str = str(num2)
    if len(num1) < len(num2):
        num1 = num1.zfill(len(num2))
    else:
        num2 = num2.zfill(len(num1))
    my_sum: str = ''
    for i in zip(num1, num2):
        my_sum += str(sum(int(j) for j in i))
    return int(my_sum)