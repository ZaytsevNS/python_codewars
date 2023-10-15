def count_bits(n):
    n_bin = bin(n)
    for _ in range(len(n_bin)):
        count = n_bin.count('1')
    return count