# -*- coding: utf-8 -*-

from typing import List


def get_answer(list_v: List[int], list_p: List[int], x: int):
    total = -0.000001
    for i, (v, p) in enumerate(zip(list_v, list_p)):
        total += v * p / 100.0
        if total > x:
            return i + 1
    return -1

if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N, X = map(int, input().split())

    _list_v = []
    _list_p = []
    for _ in range(N):
        _v, _p = map(int, input().split())
        _list_v.append(_v)
        _list_p.append(_p)

    print(get_answer(_list_v, _list_p, X))
