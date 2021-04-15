def to_time(seconds: int) -> str:
    return f'{seconds // 3600} hour(s) and {(seconds // 60) % 60} minute(s)'
