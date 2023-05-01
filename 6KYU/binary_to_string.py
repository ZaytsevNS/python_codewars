# Solution for task: https://www.codewars.com/kata/5583d268479559400d000064/

def binary_to_string(binary: str) -> str:
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))
