# Solution for task: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/

def wave(people: str) -> list:
    """ This function turns a string into a Mexican Wave """
    wave: list = []
    for i in range(len(people)):
        if people[i].isalpha():
            wave.append(people[:i] + people[i].upper() + people[i+1:])
    return wave
