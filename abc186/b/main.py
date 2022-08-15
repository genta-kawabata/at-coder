# -*- coding: utf-8 -*-

def get_answer(num):
    return "hoge"



if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())


    h, w = map(int, input().split())

    _l_aij = []
    _min_block = 1000
    for i in range(h):
        _l_ai = list(map(int, input().split()))
        _min_i = min(_l_ai)

        if _min_i < _min_block:
            _min_block = _min_i

        _l_aij.append(_l_ai)

    _total = 0
    for i in range(h):
        for j in range(w):
            _total += (_l_aij[i][j] - _min_block)


    print(_total)
