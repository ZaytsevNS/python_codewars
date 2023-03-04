# Solution for task: https://www.codewars.com/kata/59727ff285281a44e3000011/

def band_name_generator(name: str) -> str:
    if name[0].lower() != name[-1].lower():
        return f"The {name.capitalize()}"
    else:
        return f"{name.capitalize()}{name[1:]}"
