def palindrome(num):
    if isinstance(num, int) and num > 0:
        return True if str(num) == str(num)[::-1] else False
    return "Not valid"
