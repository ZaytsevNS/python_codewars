def validate_pin(pin):
    if len(pin) < 4 or len(pin) == 5 or len(pin) > 6 or not pin.isdecimal():
        return False
    return True