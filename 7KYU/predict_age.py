from math import sqrt


def predict_age(*args):
    return sqrt(sum(i * i for i in args)) // 2
