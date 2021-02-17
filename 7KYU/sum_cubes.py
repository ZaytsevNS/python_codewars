def sum_cubes(n):
    my_array = [n ** 3 for n in range(1, n+1)]
    return sum(my_array)