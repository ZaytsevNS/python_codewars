# Solution for task: https://www.codewars.com/kata/62a611067274990047f431a8/

def alternate(n: int, first_value, second_value) -> list:
    final_list: list = []
    
    while len(final_list) < n:
        final_list.append(first_value)
        if len(final_list) < n:
            final_list.append(second_value)
        
    return final_list
