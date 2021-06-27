def close_compare(a, b, margin = 0) -> int:
    if margin == 0:
        if a > b: 
            return 1
        elif a < b: 
            return -1
        else: 
            return 0
    else:
        if abs(a - b) <= margin: 
            return 0
        elif a - b > margin: 
            return 1
        else: 
            return -1
