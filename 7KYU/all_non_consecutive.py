# Solution for task: https://www.codewars.com/kata/58f8b35fda19c0c79400020f/

def all_non_consecutive(arr: list) -> list:
    
    result = list()
    
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] != 1:
            result.append({'i': arr.index(arr[i + 1]),
                           'n': arr[i + 1]
                          })
    
    return result