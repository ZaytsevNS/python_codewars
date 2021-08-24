def prev_mult_of_three(n: int):
    if not n % 3:
        return n
    else:
        while n % 3:
            n //= 10
        return n or None
        