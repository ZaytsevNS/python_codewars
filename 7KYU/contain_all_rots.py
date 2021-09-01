def contain_all_rots(strng: str, arr: list) -> bool:
    if not strng:
        return True
    rotation: set = set([strng[i:] + strng[:i] for i in range(len(strng)+1)])
    return (rotation.intersection(set(arr)) == rotation)
