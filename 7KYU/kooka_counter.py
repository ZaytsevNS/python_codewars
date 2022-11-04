# Solution for task: https://www.codewars.com/kata/58e8cad9fd89ea0c6c000258/

def kooka_counter(laughing: str) -> int:
    male: int = len([i for i in laughing.split('ha') if i])
    female: int = len([i for i in laughing.split('Ha') if i])
    return male + female
