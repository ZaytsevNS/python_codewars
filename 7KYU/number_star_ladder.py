# https://www.codewars.com/kata/5631213916d70a0979000066/

def pattern(n: int) -> str:
    row = '1\n'
    for i in range(2, n+1):
        row += f"1{'*'*(i-1)}{i}\n"
    return row[:-1]