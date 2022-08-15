# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # S = input()
    N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))

    L_A, L_B = [], []
    min_time = int(1e5) + 1

    for i in range(N):
        A, B = map(int, input().split())
        L_A.append(A)
        L_B.append(B)

    for i, a in enumerate(L_A):

        for j, b in enumerate(L_B):
            if i == j:
                min_time = min(min_time, a + b)
            else:
                min_time = min(min_time, max(a, b))

    print(min_time)

