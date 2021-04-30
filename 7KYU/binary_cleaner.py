def binary_cleaner(seq: list) -> tuple:
    list_with_zero_and_one = []
    list_with_idx_element_greater_one = []
    for i, k in enumerate(seq):
        if k <= 1:
            list_with_zero_and_one.append(k)
        else:
            list_with_idx_element_greater_one.append(i)
    return list_with_zero_and_one, list_with_idx_element_greater_one
