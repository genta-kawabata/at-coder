"""
ABC185 - C
"""

def combination(n: int, m: int):

    ans = 1
    bunshi = n - (m - 1)
    bunbo = 1
    for _ in range(m):
        ans *= bunshi
        ans //= bunbo
        bunshi += 1
        bunbo += 1
    
    return ans


def combination_math(n: int, m: int):
    import math
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))
