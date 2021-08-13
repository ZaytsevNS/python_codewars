def halving_sum(n: int) -> int: 
    halv_sum: int = n
    while n != 1:
        n //= 2
        halv_sum += n
    return halv_sum
