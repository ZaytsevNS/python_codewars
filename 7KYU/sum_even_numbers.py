def sum_even_numbers(seq: list) -> int: 
    return 0 if len(seq) == 0 else sum([i for i in seq if not i % 2])