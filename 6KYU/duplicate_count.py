def duplicate_count(s: str) -> int:
    if len(s) <= 1:
        return 0
    dict_symbol_from_s = {}
    for i in s:
        if i.lower() not in dict_symbol_from_s:
            dict_symbol_from_s[i.lower()] = 1
        else:
            dict_symbol_from_s[i.lower()] += 1
    count_duplicate = 0
    for v in dict_symbol_from_s:
        if dict_symbol_from_s[v] > 1:
            count_duplicate += 1
    return count_duplicate
     