def reverse_bits(n: int) -> int:
    """
    This function reverses the bits in an integer.
    """
    return int(''.join([str(bin(n)[2:])[::-1]]), 2)
    