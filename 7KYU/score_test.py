def score_test(tests: list, right: int, omit: int, wrong: int) -> int:
    ans = [tests.count(i) for i in range(3)]
    return ans[0]*right + ans[1]*omit - ans[2]*wrong
