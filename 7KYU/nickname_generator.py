# Solution for task: https://www.codewars.com/kata/593b1909e68ff627c9000186/

def nickname_generator(name: str) -> str:
    vowels: str = 'aeiou'
    if len(name) < 4:
        return "Error: Name too short"
    if name[2] in vowels:
        return name[:4]
    else:
        return name[:3]
