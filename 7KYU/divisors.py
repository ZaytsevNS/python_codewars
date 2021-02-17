def divisors(integer):
    array_divisors = []
    for i in range(integer-1, 1, -1):
        if integer % i == 0:
            array_divisors.append(i)

    if len(array_divisors) == 0:
        return (f'{integer} is prime')

    return sorted(array_divisors)