def remove_consecutive_duplicates(s: str) -> str:
    """ This function removes all consecutive duplicate words from string, leaving only first words entries. """
    unique = []
    current_word = None
    for i in s.split(' '):
        if i != current_word:
            unique.append(i)
            current_word = i
    return ' '.join(unique)
