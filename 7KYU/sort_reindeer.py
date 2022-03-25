def sort_reindeer(reindeer_names: list) -> list:
    """ Function returns a sequence with the Reindeer names sorted by their last names. """
    return sorted(reindeer_names, key=lambda last_names: last_names.split()[1])
