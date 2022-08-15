# -*- coding: utf-8 -*-


def combination(n: int, m: int) -> int:
    ans = 1
    bunbo = 1
    bunshi = n - (m - 1)
    for _ in range(m):
        ans *= bunshi
        ans //= bunbo
        bunshi += 1
        bunbo += 1

    return ans


def get_answer(l: int) -> int:

    # l-1 C 11 を求める
    return combination(l - 1, 11)


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    L = int(input())

    print(get_answer(L))
