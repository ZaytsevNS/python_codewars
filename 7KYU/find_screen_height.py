def find_screen_height(width: int, ratio: str) -> str:
    k_ratio = []
    for i in ratio.split(':'):
        k_ratio.append(int(i))
    height = (width * k_ratio[1]) // k_ratio[0]
    return f'{width}x{height}'