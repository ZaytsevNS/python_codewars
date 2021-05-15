def case_sensitive(s: str) -> list:
    upper_letter = [i for i in s if i.isupper()]
    if len(upper_letter) < 1:
        return [True, []]
    return [False, upper_letter]
    