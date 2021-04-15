def is_isogram(string: str) -> bool:
    if len(string) == 0:
        return True
    letter_count_dict = {}
    for i in string:
        if i.lower() in letter_count_dict:
            letter_count_dict[i.lower()] += 1
        else:
            letter_count_dict[i] = 1
    for v in letter_count_dict.values():
        if v >= 2:
            return False
    return True
