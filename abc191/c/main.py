# -*- coding: utf-8 -*-

from typing import List

"""
【解けなかった要因1 勘違い】
デジタル的な見方をしていた。
例えば

.....
.#...
.##..
.###.
.....

これは、三角形とみなしていたが、"#"1つで四角形とみなすため、
この例の場合、階段のような多角形になり、答えは八角形となる。

【解けなかった要因2 ひらめきがなかった】
「周囲にいくつ黒（または白）があるか判定すれば解ける」と気づいたまではよかったが、
ま、勘違いがあったせいもあるけど、マスばっかりに注目していた。
今回の解説ではマスを区切った格子点を座標とみなしていた。
発想が乏しかった。次に繋げる。
"""


def count_around_black(x, y, S):
    count = 0

    if S[x-1][y-1] == "#":
        count += 1
    if S[x][y-1] == "#":
        count += 1
    if S[x][y] == "#":
        count += 1
    if S[x-1][y] == "#":
        count += 1

    return count


def get_answer(H, W, S: List[str]):

    ans = 0
    for x in range(1, H):
        for y in range(1, W):
            # print(f"{x}, {y}")
            n_around_black = count_around_black(x, y, S)
            # print(n_around_black)

            if n_around_black in [1, 3]:
                ans += 1

    if ans == 1 or ans == 2:
        ans = 4

    return ans


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())
    pass


    _H, _W = map(int, input().split())

    _S = []
    for _ in range(_H):
        _S.append(input())

    print(get_answer(_H, _W, _S))
