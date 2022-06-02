# https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/


def sum_of_differences(arr: list) -> int:
    arr = sorted(arr, reverse=True)
    return sum(arr[i]-arr[i+1] for i in range(len(arr)-1))
