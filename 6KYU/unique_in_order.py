def unique_in_order(iterable):
    unique = []
    current_letter = None
    for i in iterable:
        if i != current_letter:
            unique.append(i)
            current_letter = i
    return (unique)