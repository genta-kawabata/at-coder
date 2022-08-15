# -*- coding: utf-8 -*-

from typing import List

def base_n_to_dec(str_base_no: str, n: int):
    """
    N進数の文字列を10進数に変換する
    ans = int(str_base_no, n)
    では、2 <= n <= 36 の制約あり
    1文字で表せるのは、0-9 の10文字と、a-z の26文字だからかな～
    ただしこの関数は、文字列を含むとエラー出る
    """
    result = 0
    for i, c in enumerate(str_base_no[::-1]):
        result += int(c) * (n**i)
    return result


def dec_to_bin(dec_no: int, digit: int) -> List[int]:
    """
    10進を2進数に変換
    dec_no: 10進数
    digit: 桁数

    dec_to_bin(3, 3) -> [0, 1, 1]
    dec_to_bin(3, 4) -> [0, 0, 1, 1]

    ※ 桁数が足りない場合は実装できていない
    dec_to_bin(3, 1) -> エラー
    """
    result: List[int] = [0 for _ in range(digit)]

    counter = 0
    while dec_no != 0:
        result[digit - 1 - counter] = dec_no % 2
        dec_no = dec_no // 2
        counter += 1
    return result
