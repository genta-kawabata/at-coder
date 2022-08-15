# -*- coding: utf-8 -*-
import math

def combination_math(n: int, m: int):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))

def get_answer(n):
    result = 0

    num_edge = combination_math(n, 2)

    num_saikoro = num_edge # サイコロふる回数(最低でも辺数)
    while True:

        a1 = pow(1 / n, num_edge)
        a2 = pow((1.0 - 1.0 / n), num_saikoro - num_edge)
        a3 = num_saikoro
        if (num_saikoro - 1 < 2):
            a4 = 1
        else:
            a4 = combination_math(num_saikoro - 1, 3 - 1)

        kitai = a1 * a2 * a3 * a4
        result += kitai

        if kitai < 1e-6:
            break

        num_saikoro += 1

    return result

if __name__ == "__main__":
    N = int(input())

    print(get_answer(N))
