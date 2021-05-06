from typing import List


def sortme(names: List[str]) -> List[str]:
#     bubble-sort
    flag = True
    while flag:
        flag = False
        for i in range(len(names) - 1):
            if names[i] > names[i + 1]:
                names[i], names[i + 1] = names[i + 1], names[i]
                flag = True
    return names
#     return sorted(names)
