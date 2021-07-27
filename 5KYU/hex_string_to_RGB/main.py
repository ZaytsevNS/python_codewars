def hex_string_to_RGB(hex_string: str) -> dict:
    try:
        dict_rgb: dict = {}
        dict_rgb['r'] = int(hex_string[1:3], 16)
        dict_rgb['g'] = int(hex_string[3:5], 16)
        dict_rgb['b'] = int(hex_string[5:7], 16)
        return dict_rgb
    except:
        return {}
    