def capitalize(s: str) -> list:
    string_one: str = ''
    string_two: str = ''
    for i, k in enumerate(s):
        if not i % 2:
            string_one += k.upper()
            string_two += k
        else:
            string_one += k
            string_two += k.upper()
    return [string_one, string_two]
    