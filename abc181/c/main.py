# -*- coding: utf-8 -*-


from typing import List

import itertools


def get_answer(n: int, l_xy: List[List[int]]):

    l_index = [i for i in range(n)]
    all_comb = list(itertools.combinations(l_index, 3))

    for comb in all_comb:
        x0 = l_xy[comb[0]][0]
        y0 = l_xy[comb[0]][1]
        x1 = l_xy[comb[1]][0]
        y1 = l_xy[comb[1]][1]
        x2 = l_xy[comb[2]][0]
        y2 = l_xy[comb[2]][1]

        if (y1 - y0) * (x2 - x0) == (y2 - y0) * (x1 - x0):
            return "Yes"

    return "No"


if __name__ == "__main__":

    N = int(input())
    L_XY = []
    for _ in range(N):
        L_XY.append(list(map(int, input().split())))

    print(get_answer(N, L_XY))
