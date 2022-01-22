def count_duplicates(name: list, age: list, height: list) -> int:
    a: list = [list(i) for i in zip(name, age, height)]
    not_duplicates: list = []
    count_duplicates: int = 0 
    for i in a:
        if i not in not_duplicates:
            not_duplicates.append(i)
        else:
            count_duplicates += 1
    return count_duplicates
    