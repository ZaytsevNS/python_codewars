# https://www.codewars.com/kata/581e476d5f59408553000a4b/

def length(head) -> int:
    if head:
        return 1 + length(head.next)
    return 0