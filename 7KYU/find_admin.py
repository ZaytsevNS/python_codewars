from typing import List


def find_admin(lst: List[dict], lang: str) -> List[dict]: 
    return [i for i in lst if i['language'] == lang and i['githubAdmin'] == 'yes']
    