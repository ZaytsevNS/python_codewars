SCORES: dict = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
                'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
                'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
                'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}


def sexy_name(name: str) -> str:
    if name:
        score: int = sum(SCORES.get(i.upper()) for i in ''.join(i for i in name.split()))
        RULES: dict = {score <= 60: 'NOT TOO SEXY',
                       61 <= score <= 300: 'PRETTY SEXY',
                       301 <= score <= 599: 'VERY SEXY',
                       score >= 600: 'THE ULTIMATE SEXIEST'}
        return RULES.get(bool(score))
    return 'NOT TOO SEXY'