# Solution for task: https://www.codewars.com/kata/58e0cb3634a3027180000040/

def sort_by_value_and_index(arr: list) -> list:
    """ This function sort an array of integer numbers by the product of the value and the index of the positions. """
    arr_with_product: list = [[k, i * k] for i, k in enumerate(arr, 1)]
    return [i[0] for i in sorted(arr_with_product, key=lambda x: x[1])]