def get_missing_element(seq: list) -> int: 
    return int(''.join(map(str,(set([i for i in range(10)]) - set(seq)))))