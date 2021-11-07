def save(sizes: list, hd: int) -> int: 
    return sum([sum(sizes[:i+1]) <= hd for i in range(len(sizes))])
    