# Solution for task: https://www.codewars.com/kata/54fdaa4a50f167b5c000005f/

def get_status(is_busy: bool) -> dict:
    dict_with_status: dict = {'status': 'busy' if is_busy else 'available'}
    return dict_with_status
