def tower_builder(n_floors: int) -> list:    
    tower: list = []
    level: str = ''
    for i in range(n_floors):
        star = "*" * (i*2+1)
        space = " " * (n_floors-i-1)
        level = space + star + space
        tower.append(level)
    return tower
