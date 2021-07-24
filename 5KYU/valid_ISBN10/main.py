def valid_ISBN10(isbn: str) -> bool:
    if (len(isbn) != 10) or ("X" in isbn and isbn[-1].isdigit()) or (isbn.isalpha()):
        return False
    if "X" in isbn:
        isbn = isbn[:-1]
        sum = 100
        for i, k in enumerate(isbn, start=1):
            sum += i * int(k)
        return not(sum % 11)
    else:    
        sum = 0   
        for i, k in enumerate(isbn, start=1):
            sum += i * int(k)
        return not(sum % 11)