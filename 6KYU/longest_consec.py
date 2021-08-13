def longest_consec(arr: list, k: int) -> str:
    if not arr or k > len(arr) or k <= 0:
        return '' 
    consecutive_strings: list = []
    for i in range(len(arr) - k + 1):
        consecutive_strings.append(f'{"".join(arr[i:k+i])}')
    return max(consecutive_strings, key=len)
