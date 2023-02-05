# Solution for task: https://www.codewars.com/kata/59557b2a6e595316ab000046/train/python

def convert_hash_to_array(hash: dict) -> list:
    """ Convert a hash into an array. """
    return sorted(list([k, v] for k, v in hash.items()))
