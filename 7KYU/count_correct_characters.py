# Solution for task: https://www.codewars.com/kata/5912ded3f9f87fd271000120/

def count_correct_characters(correct: str, guess: str) -> int:
    if len(correct) != len(guess):
        raise Exception("Error!")
    set_correct = set((i, k) for i, k in enumerate(correct))
    set_guess = set((i, k) for i, k in enumerate(guess))
    return len(set_correct.intersection(set_guess))
