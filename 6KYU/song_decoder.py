def song_decoder(song: str) -> str:
    return ' '.join(song.replace("WUB", ' ').split())
    