def adjacent_element_product(array: list) -> int:
    return max([array[i] * array[i + 1] for i in range(len(array) - 1)])