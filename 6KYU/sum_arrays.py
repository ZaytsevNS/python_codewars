def sum_arrays(arr1: list, arr2: list) -> list:
    """ This function returns the sum of those two arrays. """
    if len(arr1) == 0 and len(arr2) == 0:
        return []
    if (len(arr1) == 1 and arr1[0] == 0) and (len(arr2) == 1 and arr2[0] == 0):
        return []
    if (len(arr1) == 1 and len(arr2) == 0) and (arr1[0] == 0):
        return [0]
    if (len(arr1) == 0 and len(arr2) == 1) and (arr2[0] == 0):
        return [0]
    if (len(arr1) > 1 and len(arr2) == 0 and arr1[0] == 0):
        return arr1
    if (len(arr1) == 0 and len(arr2) > 1 and arr2[0] == 0):
        return arr2
    arr1_copy = arr1.copy()
    arr2_copy = arr2.copy()
    if len(arr1_copy) == 0:
        arr1_copy.append(0)
    if len(arr2_copy) == 0:
        arr2_copy.append(0)
    first_number, second_number = [int(i) for i in arr1_copy], [int(i) for i in arr2_copy]
    sum_number = int(''.join(map(str, first_number))) + int(''.join(map(str, second_number)))
    if sum_number > 0:
        return [int(i) for i in str(sum_number)]
    # if sum_number < 0:
    sum_number = str(sum_number)
    first_negative_number = int(sum_number[0:2])
    answer = [int(i) for i in str(sum_number)[2:]]
    answer.insert(0, first_negative_number)
    return answer