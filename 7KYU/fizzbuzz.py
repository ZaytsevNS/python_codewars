# Solution for task: https://www.codewars.com/kata/5300901726d12b80e8000498/

def fizzbuzz(n: int) -> list:
    result: list = []
    for i in range(1, n + 1):
        if not i % 3 and not i % 5:
            result.append('FizzBuzz')
        elif not i % 3:
            result.append('Fizz')
        elif not i % 5:
            result.append('Buzz')
        else:
            result.append(i)        
    return result
