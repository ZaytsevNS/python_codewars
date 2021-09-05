def frame(phrase='', ch='*') -> str: 
    if not phrase:
        return f'{ch * 4}\n{ch + "  " + ch}\n{ch + "  " + ch}\n{ch * 4}'
    else:
        first_line = f"{ch}{ch * (len(phrase)+2)}{ch}"
        second_line = f"{ch}{' ' * (len(phrase)+2)}{ch}"
        third_line = f"{ch} {phrase} {ch}"
        return f'{first_line}\n{second_line}\n{third_line}\n{second_line}\n{first_line}'
    