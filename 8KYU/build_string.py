# Solution for task: https://www.codewars.com/kata/55c90cad4b0fe31a7200001f/


def build_string(*args) -> str:
    return "I like {0}!".format(", ".join(args))
