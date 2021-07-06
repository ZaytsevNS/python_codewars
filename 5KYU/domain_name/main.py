def domain_name(url: str) -> str:
    return url.split("www.")[-1].split("//")[-1].split(".")[0]
    