import math

"""
N が素数であれば、
2, 3, ..., sqrt(N) で割ったときいずれも割り切れない
"""
def is_prime_number(number: int) -> bool:
    if number < 2:
        return False
    else:
        max_rt = int(math.sqrt(number))
        for i in range(2, max_rt + 1, 1):
            if number % i == 0:
                return False
        return True
