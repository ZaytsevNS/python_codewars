# Solution for task: https://www.codewars.com/kata/5803956ddb07c5c74200144e/

def dating_range(age: int) -> str:
    if age <= 14:
        min_age = int(age - 0.10 * age)
        max_age = int(age + 0.10 * age)
    else:
        min_age = (age // 2) + 7
        max_age = (age - 7) * 2
    return f"{min_age}-{max_age}"
