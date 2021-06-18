import re


def validPhoneNumber(phoneNumber: str) -> bool:
    result = re.findall(r"^\(\d{3}\)\s\d{3}-\d{4}$", phoneNumber)
    return len(result) >= 1