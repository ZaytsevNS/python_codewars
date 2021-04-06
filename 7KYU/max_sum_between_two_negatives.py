def max_sum_between_two_negatives(arr: list) -> int:
    neg_idx: list = []
    my_interval: list = []
    my_sum: list = []
    for i in range(len(arr)):
        if arr[i] < 0:
            neg_idx.append(i)
    if len(neg_idx) < 2:
        return -1
    for k in range(len(neg_idx) - 1):
        my_interval.append(arr[neg_idx[k]:neg_idx[k + 1]])
    for j, k in enumerate(my_interval):
        my_sum.append(sum(my_interval[j][1:]))
    return max(my_sum) if max(my_sum) > 0 else 0
