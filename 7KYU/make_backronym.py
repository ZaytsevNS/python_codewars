# https://www.codewars.com/kata/55805ab490c73741b7000064/

def make_backronym(acronym: str) -> str:
    return ' '.join(dictionary.get(i.upper()) for i in acronym)