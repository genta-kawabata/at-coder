# -*- coding: utf-8 -*-


def is_include_7_08(k: int):
    k_8 = oct(k)
    return "7" in str(k_8)


def is_include_7_10(k):
    return "7" in str(k)


def get_answer(n):
    count = 0
    for i in range(1, n + 1, 1):
        if not (is_include_7_08(i) or is_include_7_10(i)):
            count += 1
        else:
            a = 3

    return count



# 8で割った余りが7
# 10で割った余りが7

# 10進数の場合、70, 700, 7000, 70000代



if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())


    N = int(input())


    print(get_answer(N))
