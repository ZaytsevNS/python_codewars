from typing import Union


def sum_ppg(playerOne: dict, playerTwo: dict) -> Union[int, float]:
    return playerOne['ppg'] + playerTwo['ppg']

