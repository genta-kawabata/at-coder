# -*- coding: utf-8 -*-

from typing import List


def get_answer(n: int, s: int, d: int, l_x: List[int], l_y: List[int]) -> str:

    for x, y in zip(l_x, l_y):
        if x < s and y > d:
            return "Yes"
    
    return "No"


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N, S, D = map(int, input().split())

    L_X: List[int] = []
    L_Y: List[int] = []

    for _ in range(N):
        X, Y = map(int, input().split())
        L_X.append(X)
        L_Y.append(Y)

    print(get_answer(N, S, D, L_X, L_Y))
