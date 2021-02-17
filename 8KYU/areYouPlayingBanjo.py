def areYouPlayingBanjo(name: str) -> str:
    if name.startswith('R') or name.startswith('r'):
        return f'{name} plays banjo'
    return f'{name} does not play banjo'