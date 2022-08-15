# -*- coding: utf-8 -*-

from typing import List


def dec_to_bin(dec_no, num_keta) -> List[int]:
    result = [0 for _ in range(num_keta)]

    target = dec_no
    counter = 0
    while target != 0:
        result[num_keta - 1 - counter] = (target % 2)
        target = target // 2
        counter += 1
    return result


def get_answer(n, m, k, l_a, l_b, l_c, l_d):

    l_bin = [i for i in range(pow(2, k))]

    max_count = -1
    for bin in l_bin:
        # 0 = 0 0 0 -> 皿 [ck, ck, ck]
        # 1 = 0 0 1 -> 皿 [ck, ck, dk]
        # 2 = 0 1 0 -> 皿 [ck, dk, ck]

        # 人の選んだ方のリスト
        l_select = dec_to_bin(bin, k)

        l_plate = [False for _ in range(n)]
        for kk, select in enumerate(l_select):
            # kk さんが選んだ皿
            plate_no = l_c[kk] if select == 0 else l_d[kk]
            l_plate[plate_no - 1] = True

        # 条件をループ
        counter = 0
        for a, b in zip(l_a, l_b):
            if l_plate[a - 1] and l_plate[b - 1]:
                counter += 1
            
        if max_count < counter:
            max_count = counter
    
    return max_count


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N, M = map(int, input().split())

    L_A = []
    L_B = []

    for _ in range(M):
        A, B = map(int, input().split())
        L_A.append(A)
        L_B.append(B)
    
    K = int(input())

    L_C = []
    L_D = []

    for _ in range(K):
        C, D = map(int, input().split())
        L_C.append(C)
        L_D.append(D)

    print(get_answer(N, M, K, L_A, L_B, L_C, L_D))
