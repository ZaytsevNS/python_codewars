import re


def validate_hello(greetings: str) -> bool:
    return True if re.search(r'hello|ciao|salut|hallo|hola|ahoj|czesc', greetings.lower()) else False