def pyramid(n: int) -> list:
    if n < 1:
        return []
    my_pyramid: list = []
    for i in range(1, n+1):
        my_pyramid.append([1]*i)
    return my_pyramid
