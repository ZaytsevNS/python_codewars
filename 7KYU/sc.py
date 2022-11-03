# Solution for task: https://www.codewars.com/kata/56fe97b3cc08ca00e4000dc9/

def sc(apple: list) -> list:
    for i in range(len(apple)):
        for j in range(len(apple[i])):
            if apple[i][j] == 'B':
                return [i, j]
