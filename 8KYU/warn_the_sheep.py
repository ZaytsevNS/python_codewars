def warn_the_sheep(arr: list) -> str:
    my_arr = list(reversed(arr.copy()))
    for i in range(len(my_arr)):
        if my_arr[0] == "wolf":
            return 'Pls go away and stop eating my sheep'
        else:
            my_arr = [None] + my_arr
            return f'Oi! Sheep number {my_arr.index("wolf") - 1}! You are about to be eaten by a wolf!'