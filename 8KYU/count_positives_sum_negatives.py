def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    pos = []
    neg = []
    for i in arr:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    return [len(pos), sum(neg)]