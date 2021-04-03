def calc(s: str) -> int:
    total1 = ''
    for i in s:
        total1 += str(ord(i))
    total2 = ''
    for k in total1:
        if k == str(7):
            total2 += str(1)
        else:
            total2 += k
    return sum([int(i) for i in total1]) - sum([int(i) for i in total2])
