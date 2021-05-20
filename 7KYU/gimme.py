def gimme(input_array: list) -> int:
    middle_element = sorted(input_array)[1]
    return input_array.index(middle_element)
    