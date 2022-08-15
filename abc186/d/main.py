# -*- coding: utf-8 -*-


from typing import List


def get_cumulative_sum_recursive(numbers: List[int]):
    """再帰で累積和を求める。
    RecursionError が出てしまうケース
    """
    if len(numbers) == 0:
        return [0]
    else:
        # tail = numbers.pop(-1)
        tail = numbers[-1]
        ruiseki_list = get_cumulative_sum_recursive(numbers[0:len(numbers) - 1])

        tail_of_pre = ruiseki_list[-1]
        return ruiseki_list + [tail_of_pre + tail]


def get_cumulative_sum_sequential(numbers: List[int]):
    """forで累積和を求める。
    This method works.
    """
    result: List[int] = [0]

    for number in numbers:
        result.append(result[-1] + number)

    return result


def _get_answer_primitive(l_a: List[int]):
    """forと再帰で答えを求める。
    O(N^2)
    """
    if len(l_a) == 2:
        return abs(l_a[0] - l_a[1])
    else:
        total = 0
        for k in range(0, len(l_a)):
            total += abs(l_a[k] - l_a[-1])

        _ = l_a.pop(-1)
        return _get_answer_primitive(l_a) + total


def _get_answer_cumulative(l_a: List[int]):
    """累積和で答えを求める。
    O(N*logN)
    """
    n = len(l_a)
    l_c = get_cumulative_sum_sequential(l_a)

    # (N-1) * C_N+1
    ans1 = (n - 1) * l_c[-1]

    # sigma{i=1>N-1}{C_i + (N-i) * A_i}
    ans2 = 0
    for i in range(n - 1):
        ans2 += l_c[i] + (n - i) * l_a[i]

    return ans1 - ans2


def get_answer(n: int, l_a: List[int]):
    l_a.sort()

    return _get_answer_cumulative(l_a)


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N = int(input())
    L_A = list(map(int, input().split()))

    print(get_answer(N, L_A))
