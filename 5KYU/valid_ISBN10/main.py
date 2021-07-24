def valid_ISBN10(isbn: str) -> bool:
    try:
        if (len(isbn) != 10) or ("X" in isbn and isbn[-1].isdigit()) or (isbn.isalpha()):
            return False
        return not sum([i * (10 if k == 'X' else int(k)) for i, k in enumerate(isbn, start=1)]) % 11
    except Exception:
        return False