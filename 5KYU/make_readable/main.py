def make_readable(seconds):
    hour = seconds // 3600
    minutes = (seconds - hour * 3600) // 60
    sec = seconds - hour * 3600 - minutes * 60
    return ("%02d:%02d:%02d" % (hour, minutes, sec))
    