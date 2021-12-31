def noonerize(numbers: list) -> int or str:
    if not all(type(i) == int for i in numbers):
        return "invalid array"
    else:
        first_num: int = int(str(numbers[1])[0] + str(numbers[0])[1:])
        second_num: int = int(str(numbers[0])[0] + str(numbers[1])[1:])
    return abs(first_num-second_num)
    