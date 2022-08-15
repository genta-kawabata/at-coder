# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    A, B, C = map(int, input().split())

    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    if C == 1:
        if B > A:
            print("Aoki")
        else:
            print("Takahashi")

