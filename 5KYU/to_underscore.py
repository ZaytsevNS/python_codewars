def to_underscore(string: str) -> str:
    if type(string) != str:
        return str(string)
    else:
        my_snake_case = ''
        for i in string:
            if i.isupper():
                my_snake_case += f'_{i.lower()}'
            else:
                my_snake_case += f'{i.lower()}'
        return my_snake_case[1:]