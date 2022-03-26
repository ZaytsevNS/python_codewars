def balanced_num(num: int) -> str:
    if not len(str(num)) % 2:
        num1, num2 = str(num)[:len(str(num))//2-1], str(num)[len(str(num))//2+1:]
        return 'Balanced' if sum(int(i) for i in num1) == sum(int(i) for i in num2) else 'Not Balanced'
    else:
        num1, num2 = str(num)[:len(str(num))//2], str(num)[len(str(num))//2+1:]
        return 'Balanced' if sum(int(i) for i in num1) == sum(int(i) for i in num2) else 'Not Balanced'