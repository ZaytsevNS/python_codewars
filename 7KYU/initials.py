# Solution for task: https://www.codewars.com/kata/55968ab32cf633c3f8000008/

def initials(name: str) -> str:
    
    split_name: list = name.split()
    
    return f"{'.'.join(i[0].upper() for i in split_name[:-1])}.{split_name[-1].title()}"