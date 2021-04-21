from typing import List


def word_to_bin(word: str) -> List[str]:
    list_word_to_bin = [bin(ord(letter))[2:].zfill(8) for letter in word]
    return list_word_to_bin
    