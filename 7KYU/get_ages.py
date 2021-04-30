def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0 or sum_ - difference < 0:
        return None
    return ((difference + round(sum_ - difference) / 2 ), round(sum_ - difference) / 2)
    