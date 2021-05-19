def number(lines: list) -> list:
    if len(lines) < 1:
        return []
    line_numbering = [f'{i}: {k}' for i, k in enumerate(lines, start=1)]
    return line_numbering
