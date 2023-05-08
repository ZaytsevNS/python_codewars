# Solution for task: https://www.codewars.com/kata/54592a5052756d5c5d0009c3/

head = lambda x: x[0]
tail = lambda x: x[1:] if len(x) > 1 else []
init = lambda x: x[:-1] if len(x) > 1 else []
last = lambda x: x[-1]