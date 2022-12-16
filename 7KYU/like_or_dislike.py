# Solution for task: https://www.codewars.com/kata/62ad72443809a4006998218a/

from typing import Union, List


def like_or_dislike(lst: Union[List[str], None]) -> str:
    """
    This function takes in a list of button inputs and returns the final state.
    """
    if len(lst) == 1:
        return lst[0]
    elif len(lst) > 1:
        current_state = lst[0]
        for i in lst[1:]:
            if i == current_state:
                current_state = 'Nothing'
            else:
                current_state = i
        return current_state
    else:
        return 'Nothing'
