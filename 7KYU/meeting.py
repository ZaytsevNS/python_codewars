from typing import List, Union


def meeting(rooms: List[str]) -> Union[int, str]:
    if 'O' not in rooms:
        return 'None available!'
    return rooms.index('O') 

    