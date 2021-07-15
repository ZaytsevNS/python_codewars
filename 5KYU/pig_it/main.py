def change_word(s: str) -> str:
    """ Moves the first letter of each word to the end of it. """
    return f'{s[1:]}{s[0]}'
    
def pig_it(s: str) -> str:
    pig_text = []
    for i in s.split(): 
        if i not in ('!?'):
            pig_text.append(f'{change_word(i)}ay')
        else: pig_text.append(i)        
    return ' '.join(pig_text)
    