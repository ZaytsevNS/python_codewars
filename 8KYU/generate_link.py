# Solution for task: https://www.codewars.com/kata/57037ed25a7263ac35000c80/

import urllib.parse


def generate_link(user: str) -> str:
    return f"http://www.codewars.com/users/{urllib.parse.quote(user)}"
