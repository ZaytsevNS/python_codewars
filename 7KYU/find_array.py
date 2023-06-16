# Solution for task: https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055/

def find_array(arr1: list, arr2: list) -> list:
    
    new_arr = list()
    
    for i in arr2:
        if i < len(arr1):
            new_arr.append(arr1[i])

    return new_arr
