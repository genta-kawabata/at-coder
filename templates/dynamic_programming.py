# -*- coding: utf-8 -*-

from typing import Any


def chmin(a: Any, b: Any) -> bool:
    """
    a と b を比較して、
    a > b ならば a に b を代入して true を返す
    a < b ならば何もせずに false を返す
    """
    if a > b:
        a = b
        return True
    return False


def chmax(a: Any, b: Any) -> bool:
    """
    a と b を比較して、
    a < b ならば a に b を代入して true を返す
    a > b ならば何もせずに false を返す
    """
    if a < b:
        a = b
        return True
    return False



N = 6
W = 9

L_Item = [
    (2, 3),
    (1, 2),
    (3, 6),
    (2, 1),
    (1, 3),
    (5, 85)
]
L_Item_W = []
L_Item_V = []

for wv in L_Item:
    L_Item_W.append(wv[0])
    L_Item_V.append(wv[1])

dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

for i in range(N):
    item_w = L_Item_W[i]
    item_v = L_Item_V[i]
    for w in range(W + 1):

        if w >= item_w:
            # i を選べる
            add = dp[i][w - item_w] + item_v
            keep = dp[i][w]
            greater = max(add, keep)
            dp[i + 1][w] = greater
        else:
            # i を選べない
            dp[i + 1][w] = dp[i][w]

        print("=========================")
        for row in dp:
            print(row)


