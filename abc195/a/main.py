# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    M, H = map(int, input().split())

    if H % M == 0:
        print("Yes")
    else:
        print("No")
