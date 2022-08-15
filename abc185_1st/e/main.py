# -*- coding: utf-8 -*-


def dp(l_a, l_b) -> int:
    if len(l_a) == 0 or len(l_b) == 0:
        return max(len(l_a), len(l_b))
    else:
        import copy

        # ケース1: Aiを消す
        l_a_cp = copy.copy(l_a)
        l_b_cp = copy.copy(l_b)
        l_a_cp.pop(-1)
        ans1 = dp(l_a_cp, l_b_cp) + 1

        # ケース2: Bjを消す
        l_a_cp = copy.copy(l_a)
        l_b_cp = copy.copy(l_b)
        l_b_cp.pop(-1)
        ans2 = dp(l_a_cp, l_b_cp) + 1

        # ケース3:
        l_a_cp = copy.copy(l_a)
        l_b_cp = copy.copy(l_b)
        tail_a = l_a_cp.pop(-1)
        tail_b = l_b_cp.pop(-1)
        ans3 = dp(l_a_cp, l_b_cp)
        if tail_a == tail_b:
             ans3 += 1

        return min(ans1, ans2, ans3)


def get_answer(n, m, l_a, l_b) -> int:

    print(l_a)
    print(l_b)


    return dp(l_a, l_b)


if __name__ == "__main__":
    _n, _m = input().split()
    _l_a = list(map(int, input().split()))
    _l_b = list(map(int, input().split()))

    print(get_answer(_n, _m, _l_a, _l_b))

