# Solution for task: https://www.codewars.com/kata/56a28c30d7eb6acef700004d/

def is_perfect(n: int) -> bool:
    divisors: list = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            divisors.append(i)
            divisors.append(n // i)
    return sum(divisors) == n if n != 1 else False
