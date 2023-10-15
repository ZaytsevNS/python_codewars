def are_coprime(n: int, m: int) -> bool:
    factors_n: set = set(i for i in range(1, n+1) if not n % i)
    factors_m: set = set(i for i in range(1, m+1) if not m % i)
    return True if len(factors_n & factors_m) == 1 else False
