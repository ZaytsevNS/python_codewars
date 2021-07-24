from collections import Counter


def duplicate_count(s: str) -> int:
    """ This function returns the count of distinct case-insensitive alphabetic characters 
    and numeric digits that occur more than once in the input string """
    try:
        if len(s) < 2:
            return 0
        counter = dict(Counter(s.lower()))
        duplicate: dict = {}
        for k, v in counter.items():
            if v > 1:
                duplicate[k] = v        
        return len(duplicate)
    except:
        return 0
     