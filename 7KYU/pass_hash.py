import hashlib


def pass_hash(s: str) -> str:
    """ This function converts a given string into an md5 hash. """
    hash_object = hashlib.md5(s.encode('UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
