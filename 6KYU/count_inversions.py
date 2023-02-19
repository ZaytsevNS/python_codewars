# Solution for task: https://www.codewars.com/kata/537529f42993de0e0b00181f/

def count_inversions(array: list) -> int:
    """ This function calculates inversions for any arbitrary array """
    changed = True
    count = 0
    while changed:
        changed = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                changed = True
                count += 1
    return count
