def remove_url_anchor(url: str) -> str:
    if '#' in url:
        return url[:url.index('#')]
    return url
