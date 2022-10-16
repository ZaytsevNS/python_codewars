# Solution for task: https://www.codewars.com/kata/53da6a7e112bd15cbc000012/

def sort_dict(d: dict) -> list:
    """ This function returns a sorted list of tuples from the dictionary """
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
    