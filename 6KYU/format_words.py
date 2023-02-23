# Solution for task: https://www.codewars.com/kata/51689e27fe9a00b126000004/

def format_words(words) -> str:
    if (words == [""]) or (words is None) or (len(words) == 0):
        return ""
    elif len(words) > 0:
        filter_words: list = list(filter(lambda i: len(i) > 0, words))
        if len(filter_words) == 1:
            return filter_words[0]
        elif len(filter_words) > 1:
            return f"{', '.join(i for i in filter_words[:-1])} and {filter_words[-1]}"
