# -*- coding: utf-8 -*-

def get_answer(n, l_a, l_p, l_x):

    # ruiseki_time = -0.5
    flg_buy = False
    min_price = int(1e9) + 1
    for i in range(n):
        # ruiseki_time += l_a[i]
        if l_x[i] > l_a[i]:
            min_price = min(min_price, l_p[i])
            flg_buy = True

    if flg_buy:
        return min_price
    else:
        return -1


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N = int(input())
    L_A = []
    L_P = []
    L_X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        L_A.append(a)
        L_P.append(p)
        L_X.append(x)

    print(get_answer(N, L_A, L_P, L_X))
