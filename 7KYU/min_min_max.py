# Solution for task: https://www.codewars.com/kata/58d3487a643a3f6aa20000ff/

def min_min_max(arr: list) -> list:
    
    sorted_arr: list = sorted(arr)
    
    def find_min() -> int:
        return sorted_arr[0]
    
    def find_max() -> int:
        return sorted_arr[-1]
    
    def find_min_absent() -> int:
        return [i for i in [i for i in range(sorted_arr[0], sorted_arr[-1] + 1)] if i not in sorted_arr][0]
    
    return [find_min(), find_min_absent(), find_max()]
    