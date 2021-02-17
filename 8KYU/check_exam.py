def check_exam(arr1: list, arr2: list) -> int:
    """ 
    This function returns the score for this array of answers, 
    giving +4 for each correct answer,
    -1 for each incorrect answer, and +0 for each blank answer.
    """
    count = 0
    for i in range(len(arr2)):
        if arr2[i] == arr1[i]:
            count += 4
        elif arr2[i] != arr1[i] and not len(arr2[i]) == 0:
            count -= 1
    return count if count > 0 else 0