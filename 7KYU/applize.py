def i(word: str) -> str:
    VOWELS = 'AaEeIiOoUu'
    if len(word) == 0 or word.startswith('I') or word[0].islower():
        return 'Invalid word'
    count_vowels = len([i for i in word if i in VOWELS])
    if count_vowels >= len(word) - count_vowels:
        return 'Invalid word'
    return f'{"i" + word}'
    