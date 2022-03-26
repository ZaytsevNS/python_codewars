from numpy import average as np_average

class Calculator:
    @staticmethod
    def average(*args):
        return np_average(args) if args else 0