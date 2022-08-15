# -*- coding: utf-8 -*-

from typing import List


def get_answer_list(N: int, S: List[str]) -> str:
    # リストのまま実行すると TLE が頻発
    for i, s in enumerate(S):
        if not "!" in s:
            tmp = "!" + s
            if tmp in S:
                return s
    return "satisfiable"


def get_answer_set(N: int, S: set) -> str:
    # set を使うと速度向上
    for i, s in enumerate(S):
        if "!" + s in S:
            return s
    return "satisfiable"


def get_answer(N: int, S: List[str]) -> str:
    # return get_answer_list(N, S)
    S = set(S)
    return get_answer_set(N, S)


if __name__ == "__main__":
    _N = int(input())
    _S = [input() for _ in range(_N)]

    print(get_answer(_N, _S))
