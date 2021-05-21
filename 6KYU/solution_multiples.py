def solution(number: int) -> int:
    return sum([i for i in range (2, number) if not i % 3 or not i % 5])
  