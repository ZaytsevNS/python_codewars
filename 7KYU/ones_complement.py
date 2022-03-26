def ones_complement(binary_number: str) -> str:
    return ''.join('1' if i == '0' else '0' for i in binary_number)