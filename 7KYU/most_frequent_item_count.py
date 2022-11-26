# Solution for task: https://www.codewars.com/kata/56582133c932d8239900002e/

from collections import Counter


def most_frequent_item_count(collection: list) -> int:
    """ Function to find the count of the most frequent item of an array. """
    return max(Counter(collection).values()) if collection else 0
