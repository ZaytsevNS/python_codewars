def shades_of_grey(n: int) -> list:
    ''' This function returns n shades of grey in an array '''
    if n <= 0:
        return []
    elif 1 <= n <= 254:
        return ['#' + f'{i:02x}' * 3 for i in range(1, n + 1)]
    else:
        return ['#' + f'{i:02x}' * 3 for i in range(1, 255)]
    