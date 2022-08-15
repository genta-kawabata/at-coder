# -*- coding: utf-8 -*-


def base_n_to_10(str_base_no: str, n: int):
    result = 0
    for i, c in enumerate(str_base_no[::-1]):
        result += int(c) * (n**i)
    return result


def get_answer(x: str, m: int):
    # 例外処理 1桁の場合
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    else:
        d = int(max(list(x)))

        left = d
        right = int(1e18) + 1
        while right - left > 1:
            mid = (right + left) // 2
            decimal = base_n_to_10(x, mid)
            if decimal <= m:
                left = mid
            else:
                right = mid
        return right - (d + 1)


if __name__ == "__main__":
    X = input()
    M = int(input())

    print(get_answer(X, M))
