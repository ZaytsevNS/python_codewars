from typing import Union


def mango(quantity: int, price: Union[int, float]) -> Union[int, float]:
    # mangoes_quantity: int = quantity
    give_free: int = quantity // 3
    # while mangoes_quantity != 0:
        # if mangoes_quantity >= 3:
            # mangoes_quantity -= 3
            # give_free += 1
        # else:
            # break
    return (quantity - give_free) * price
