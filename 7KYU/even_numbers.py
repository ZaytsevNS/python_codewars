def even_numbers(arr: list, n: int) -> list:
    even_from_arr: list = [i for i in arr if not i % 2]
    return even_from_arr[len(even_from_arr) - n:]
    