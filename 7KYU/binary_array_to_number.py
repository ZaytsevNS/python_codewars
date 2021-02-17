def binary_array_to_number(arr):
    string_number = "".join(str(x) for x in arr)
    result = int("".join(str(i) for i in string_number), 2)
    return result