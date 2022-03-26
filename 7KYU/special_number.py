def special_number(number: int) -> str:
    return "Special!!" if all(int(i) < 6 for i in str(number)) else "NOT!!"