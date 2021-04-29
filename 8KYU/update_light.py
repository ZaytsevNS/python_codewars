def update_light(current: str) -> str:
    light = ['red', 'yellow', 'green']
    if current == light[1]:
        return light[0]
    elif current == light[2]:
        return light[1]
    return light[2]
