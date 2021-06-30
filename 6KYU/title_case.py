def title_case(title: str, minor_words=None) -> str:
    if title:
        if minor_words is None:
            return title.title()
        my_word = [word.lower() for word in title.split()]
        if my_word[0] in minor_words.lower() or minor_words.lower() in my_word:
            return f'{my_word[0].title()} {" ".join([i.title() if i not in minor_words.lower() else i for i in my_word[1:]])}'.strip()
        return " ".join(my_word).title()
    return ''
    