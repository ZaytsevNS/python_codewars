def to_alternating_case(s: str) -> str:
    my_str = ''
    for i in s:
        if i.islower():
            my_str += i.upper()
        elif i.isupper():
            my_str += i.lower()
        else:
            my_str += i
    return my_str