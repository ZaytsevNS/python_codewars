def missing_no(nums: list) -> int:
    """ This function finds the missing number """
    return list(set(nums) ^ set(range(0, 101)))[0]
