from numpy import prod


def sum_or_product(array: list, n: int) -> str:
    sorted_array = sorted(array)
    sum_high, prod_low = sum(sorted_array[::-1][:n]), prod(sorted_array[:n])
    return 'sum' if sum_high > prod_low else 'product' if prod_low > sum_high else 'same'
