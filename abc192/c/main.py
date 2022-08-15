# -*- coding: utf-8 -*-


def g1(x):
    str_x = list(str(x))
    str_x.sort(reverse=True)
    number = int("".join(str_x))
    return number

def g2(x):
    str_x = list(str(x))
    str_x.sort()
    number = int("".join(str_x))
    return number

def f(x):
    return g1(x) - g2(x)


def get_answer(n, k):

    i = 0
    a0 = n
    while i <= k - 1:
        a1 = f(a0)
        a0 = a1
        i += 1

    return a0


if __name__ == "__main__":

    a = g1(314)
    b = g2(3021)



    N, K = map(int, input().split())

    print(get_answer(N, K))
