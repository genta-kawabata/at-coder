# -*- coding: utf-8 -*-

import math

def is_prime_number(number: int) -> bool:
    if number < 2:
        return False
    else:
        max_rt = int(math.sqrt(number))
        for i in range(2, max_rt + 1, 1):
            if number % i == 0:
                return False
        return True


def get_answer(n):

    # count = 0
    # for i in range(1, n+1, 1):
    #     if is_prime_number(i):
    #         count+=1

    # count += 2
    # return count


    # count = 0
    # for i in range(2, n + 1, 1):
    #     for a in range(2, n, 1):
    #         if i % a == 0:
    #             count += 1

    # return n - count

    # l_ok = [0 for _ in range(n + 1)]

    # a = 2
    # while a * a <= n:
    #     b = 2
    #     ab = 4
    #     while ab <= n:
    #         ab = pow(a, b)
    #         if ab <= n:
    #             l_ok[ab] = 1
    #         b += 1
    #     a += 1
    
    # return n - sum(l_ok)

    l_ok = [0 for _ in range(n + 1)]

    count_ok = 0
    a = 2
    while a * a <= n:
        left = 1
        right = n + 1

        while right - left > 1:
            mid = int(left + (right - left) / 2)

            if pow(a, mid) <= n:
                left = mid
            else:
                right = mid


        for b in range(2, right, 1):
            l_ok[pow(a, b)] = 1


        # count_ok += right - 1
        a += 1

    return n - sum(l_ok)


if __name__ == "__main__":
    # S = input()
    N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    print(get_answer(N))
