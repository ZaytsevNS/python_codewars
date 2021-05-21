def to_camel_case(text: str) -> str:
    """
    This function converts dash/underscore delimited words into camel casing.
    """
    text_without_dash_and_underscore = text.replace('-', ' ').replace('_', ' ')
    list_of_words: list = []
    for i in text_without_dash_and_underscore.split():
        list_of_words.append(i)
    list_of_camel_words: list = []
    for idx, w in enumerate(list_of_words):
        if idx == 0:
            list_of_camel_words.append(w)
        else:
            list_of_camel_words.append(w.title())
    return ''.join(list_of_camel_words)   
    