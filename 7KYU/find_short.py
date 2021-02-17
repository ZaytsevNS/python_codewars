def find_short(s):
    split_str = s.split()
    split_str.sort(key=len)
    return (len(split_str[0]))