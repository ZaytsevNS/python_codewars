import re


def count_smileys(arr: list) -> int:
    """
    This function returns the total number of smiling faces.
    """
    return len(re.findall('[:;][-~]?[)D]', ' '.join(arr)))
    