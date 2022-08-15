from typing import List

import itertools


def get_answer(n: int, k: int, ll_t: List[List[int]]) -> int:

    l_p = list(itertools.permutations([i for i in range(1, n)]))

    result = 0
    for p in l_p:
        p = [0] + list(p) + [0]

        time = 0
        for j in range(len(p) - 1):
            t = ll_t[p[j]][p[j+1]]
            time += t

        if time == k:
            result += 1

    return result


if __name__ == "__main__":
    N, K = map(int, input().split())

    T = []
    for _ in range(N):
        T.append(list(map(int, input().split())))

    print(get_answer(N, K, T))
