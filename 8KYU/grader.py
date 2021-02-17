def grader(score):
    if (score > 1) or (score < 0.6):
        return 'F'
    elif 0.8 < score <= 1:
        return 'A'
    elif 0.7 < score <= 0.8:
        return 'B'
    elif 0.6 < score <= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'