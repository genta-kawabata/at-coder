def my_comb(m: int, n: int) -> int:
    if n == 1:
        return m
    elif n == 0 or (m - n) == 0:
        return 1
    elif m - n == 1:
        return n + 1
    else:
        ans = int(my_comb(m - 1, n - 1) * m / n)
        # print(ans)
        return ans


def get_answer(l: int) -> int:
    # l-1 C 11
    return int(my_comb(l - 1, 11))


def do() -> int:
    _l = int(input())
    return get_answer(_l)


if __name__ == '__main__':
    print(do())

