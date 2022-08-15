# -*- coding: utf-8 -*-

def get_answer(N, X, A):
    new_list = []
    for a in A:
        if a != X:
            new_list.append(a)
    
    ans = " ".join([str(v) for v in new_list])
    return ans

if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())


    _N, _X = map(int, input().split())
    _A = list(map(int, input().split()))


    print(get_answer(_N, _X, _A))


