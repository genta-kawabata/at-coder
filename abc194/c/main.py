# -*- coding: utf-8 -*-

from typing import List

def get_cumulative_sum_list(list_no):
    """forで累積和を求める。
    This method works.
    """
    result1 = [0]
    result2 = [0]
    for number in list_no:
        result1.append(result1[-1] + number)
        result2.append(result2[-1] + number * number)
    return result1, result2


def get_sum_from_cum_sum_list(cum_sum_list, start, stop):
    """
    元の配列 L_A の A_start + ... + A_{stop-1} を求める
    """
    return cum_sum_list[stop] - cum_sum_list[start]


def get_answer(n, l_a: List[int]):
    result = 0

    cum_list_1, cum_list_2 = get_cumulative_sum_list(l_a)

    
    for i in range(1, n, 1):
        a = l_a[i]

        sum1 = get_sum_from_cum_sum_list(cum_list_1, 0, i)
        sum2 = get_sum_from_cum_sum_list(cum_list_2, 0, i)

        iro = a * a * i
        hani = (- 2) * a * sum1
        hohe = sum2

        result += iro + hani + hohe



    return result

if __name__ == "__main__":
    # S = input()
    N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    L_A = list(map(int, input().split()))

    print(get_answer(N, L_A))
