# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())
    pass


    V, T, S, D = map(int, input().split())

    if V * T <= D <= V * S:
        print("No")
    else:
        print("Yes")



