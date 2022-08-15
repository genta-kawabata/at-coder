# -*- coding: utf-8 -*-

def get_answer(str_n: str) -> int:

    l_str_n = list(str_n)
    cnt = [0 for _ in range(3)]
    for s in l_str_n:
        cnt[int(s) % 3] += 1

    cur = (cnt[1] + 2 * cnt[2]) % 3 # 全ての桁の和を3で割ったあまり
    k = sum(cnt)

    if cur == 0:
        return 0
    elif cur == 1:
        if cnt[1] > 0:
            if k == 1:
                return -1
            else:
                return 1
        else:
            if k == 2:
                return -1
            else:
                return 2
    else:
        if cnt[2] > 0:
            if k == 1:
                return -1
            else:
                return 1
        else:
            if k == 2:
                return -1
            else:
                return 2


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())
    pass

    N = input()
    print(get_answer(N))

