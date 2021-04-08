def outed(meet: dict, boss: str) -> str:
    rating: int = 0
    for key, value in meet.items():
        if key == boss:
            rating += 2 * value
        else:
            rating += value
    rating /= len(meet)
    return 'Get Out Now!' if rating <= 5 else 'Nice Work Champ!'
