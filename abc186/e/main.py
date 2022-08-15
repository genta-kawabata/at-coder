# -*- coding: utf-8 -*-

def get_answer(n, s, k):
    for i in range(1, pow(10, 9), 1):
        if (i * n - s) % k == 0:
            return int((i * n - s) / k)
    return -1



if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    T = int(input())
    for i in range(T):
        N, S, K = map(int, input().split())
        print(get_answer(N, S, K))

