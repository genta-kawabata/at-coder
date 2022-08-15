# -*- coding: utf-8 -*-

def get_total_num_comma(keta):
    if keta <= 3:
        return 0
    else:
        max_keta_1 = pow(10, keta) - 1
        min_keta_1 = pow(10, keta - 1) - 1
        total_num_keta_1 = get_total_num_comma(keta - 1)
        num_comma = get_num_comma(keta)
        total_num_keta = (max_keta_1 - min_keta_1) * num_comma

        result = total_num_keta + total_num_keta_1

        return result


def get_num_comma(keta):
    return (keta - 1) // 3

def get_answer(n: int):

    if (n <= 999):
        return 0

    keta = len(str(n))

    total_num_keta_1 = get_total_num_comma(keta - 1)
    total_num_keta = (n - (pow(10, keta - 1) - 1)) * get_num_comma(keta)
    result = total_num_keta_1 + total_num_keta

    return result

if __name__ == "__main__":
    # S = input()
    N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    print(get_answer(N))
