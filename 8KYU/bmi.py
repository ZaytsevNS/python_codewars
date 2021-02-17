def bmi(weight, height) -> str:
    """ This function calculates body mass index. """
    body_mass_index = weight / pow(height, 2)
    if body_mass_index <= 18.5:
        return "Underweight"
    elif body_mass_index <= 25.0:
        return "Normal"
    elif body_mass_index <= 30.0:
        return "Overweight"
    return "Obese"