def vowel_indices(word: str) -> list:
    """
    This function returns list with index of the vowels in a given string. 
    """
    return [i for i, k in enumerate(word, start=1) if k.lower() in 'aeiouy']
