"""
逆元を求める
「拡張 Euclid の互除法を用いる方法」らしい
O(log p)　(p: 法)
"""


def mod_inv(a: int, mod: int):
    b, u, v = mod, 1, 0

    while b > 0:
        t = int(a / b)
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u

    u %= mod
    if u < 0:
        u += mod

    return u


"""
累乗 a^n mod を二分累乗法で求める。
O(log n)
"""


def mod_pow(a: int, n: int, mod: int):
    result = 1
    while n > 0:
        if n & 1:
            result = result * a % mod
        a = a * a % mod
        n >>= 1
    return result
