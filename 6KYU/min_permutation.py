from itertools import permutations


def min_permutation(n):
    if (len(str(n)) == 1) or (len(str(n)) == 2 and str(n)[0] == '-'):
        return n
    elif (len(str(n)) == 3 and str(n)[-1] == '0' and str(n)[0] == '-') or (len(str(n)) == 2 and str(n)[-1] == '0'):
        return n
    list_of_int_permutations = []
    if n > 0:
        for i in list(permutations([int(i) for i in str(n)])):
            if i[0] != 0:
                list_of_int_permutations.append(int(''.join(map(str, i))))
        return min(list_of_int_permutations)
    else:
        for i in list(permutations([int(i) for i in str(abs(n))])):
            if i[0] != 0:
                list_of_int_permutations.append(int(''.join(map(str, i))) * (-1))
        return max(list_of_int_permutations)
        