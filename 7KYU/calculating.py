def calculate(s: str) -> str:
    math_str = s.replace('plus', '+').replace('minus', '-')
    return str(eval(math_str))
    