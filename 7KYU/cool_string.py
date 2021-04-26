def cool_string(s: str) -> bool:
    """ 
    Let's call a string cool if it is formed only by Latin letters and no two lowercase and no two uppercase letters are in adjacent positions. 
    Given a string, check if it is cool.
    """
    string_without_whitespace = ''.join(s.split())
    if string_without_whitespace.isalpha():
        for i, k in enumerate(range(len(string_without_whitespace)-1)):
            if (string_without_whitespace[i].islower() and string_without_whitespace[i+1].islower()) or (string_without_whitespace[i].isupper() and string_without_whitespace[i+1].isupper()):
                return False
        return True
    return False
