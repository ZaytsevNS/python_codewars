def weather_info(temp):
    c = convert_to_celsius(temp)
    if c < 0:
        return (str(c) + " is freezing temperature")
    return (str(c) + " is above freezing temperature")


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius