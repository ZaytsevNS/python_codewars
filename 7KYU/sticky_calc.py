from typing import Union


def sticky_calc(operation: str, val1: Union[int, float], val2: Union[int, float]) -> int:
    val1, val2 = round(val1), round(val2)
    stick: int = int(str(val1)+str(val2))    
    operation_: dict = {'+': stick + val2,
                        '-': stick - val2,
                        '*': stick * val2,
                        '/': round(stick / val2)}
    return operation_.get(operation)
