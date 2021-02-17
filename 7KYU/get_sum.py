def get_sum(a,b):
    if a == b:
        return (a)
    n = []
    if a > b:
        for i in range(b, a+1):
            n.append(i)
        return sum(n)
    
    else:
        for i in range(a, b+1):
            n.append(i)
        return sum(n)