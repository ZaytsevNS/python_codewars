def numbers(*args) -> bool:
    return all([type(i) == int or type(i) == float for i in args])