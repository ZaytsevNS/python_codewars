# Solution for task: https://www.codewars.com/kata/5ace2d9f307eb29430000092/

def modify_multiply(st: str, loc: int, num: int) -> str:
    modify_word: str = ((st.split()[loc] + '-') * num)[:-1]
    return modify_word
