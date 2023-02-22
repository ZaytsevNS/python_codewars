# Solution for task: https://www.codewars.com/kata/5703c093022cd1aae90012c9/

def find(arr, el):
    try: return arr.index(el)
    except: return "Not found"