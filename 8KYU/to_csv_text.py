# Solution for task: https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/

def to_csv_text(array: list) -> str:
    """
    This function returns the CSV representation of a two-dimensional numeric array.
    """
    csv: str = ''    
    for i in array:
        csv += f"{','.join(map(str, i))}\n"    
    return csv[:-1]
