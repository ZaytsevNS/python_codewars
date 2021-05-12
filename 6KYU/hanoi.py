def hanoi(disks: int) -> int:
    """
    The minimum number of moves to complete a Tower of Hanoi is known as a Mersenne Number.
    """
    return 2 ** disks - 1
    