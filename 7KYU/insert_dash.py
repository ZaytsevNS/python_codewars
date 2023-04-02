# Solution for task: https://www.codewars.com/kata/55960bbb182094bc4800007b/

def insert_dash(num: int) -> str:
    
    num_in_str = str(num)
    
    result = str()
    
    for i in range(len(num_in_str) - 1):
        if int(num_in_str[i]) % 2 and int(num_in_str[i + 1]) % 2:
            result += f'{num_in_str[i]}-'
        else:
            result += num_in_str[i]
    
    return result + num_in_str[-1]
