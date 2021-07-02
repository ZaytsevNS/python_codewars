def highest_rank(arr: list) -> int:
    """ This function returns the number which is most frequent in the given input array. """
    number_with_frequent: dict = {}
    most_frequent_number: list = []
    for i in arr:
        if i not in number_with_frequent:
            number_with_frequent[i] = 1
        else:
            number_with_frequent[i] += 1
    for k, v in number_with_frequent.items():
        max_value = max([v for v in number_with_frequent.values()])
        if v == max_value:
            most_frequent_number.append(k)
    return sorted(most_frequent_number, reverse=True)[0]
