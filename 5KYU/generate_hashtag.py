def generate_hashtag(s: str):
    if s:
        hashtag = ''.join([i.title() for i in s.split()])
        return f'#{hashtag}' if len(hashtag) < 140 else False
    return False
    