# -*- coding: utf-8 -*-

from typing import List


def get_n_q_from_stdin(stdin: str) -> (int, int):
    n, q = [int(x) for x in stdin.split(" ")]
    return n, q


def get_char_list(n):
    return [chr(i) for i in range(65, 65 + n)]


def get_half_splitted_list(in_list):
    if len(in_list) == 0:
        return [], []
    elif len(in_list) == 1:
        return in_list, []
    else:
        center = int(len(in_list) / 2)
        list_1 = in_list[0:center]
        list_2 = in_list[center:]
        return list_1, list_2


def get_split_top_left_right(in_list: List[str]) -> (List[str], str, List[str]):
    if len(in_list) == 0:
        return [], None, []
    else:
        center = int(len(in_list) / 2)
        left = in_list[0:center]
        v = in_list[center]
        right = in_list[center + 1:]
        return left, v, right


def ask(c1, c2) -> str:
    while True:
        ans = input(f"? {c1} {c2}\n")
        if ans == "<" or ans == ">":
            return ans
        else:
            print("Answer is not valid...", flush=True)


def insert_value(v: str, sorted_list: List[str], compare_func) -> List[str]:
    if len(sorted_list) == 0:
        # 無条件で追加
        return [v]
    else:
        left_list, top, right_list = get_split_top_left_right(sorted_list)
        user_answer = compare_func(v, top)
        if user_answer == "<":
            return insert_value(v, left_list, compare_func) + [top] + right_list
        elif user_answer == ">":
            return left_list + [top] + insert_value(v, right_list, compare_func)


def get_answer(str_n_q: str):
    # 準備
    n, q = get_n_q_from_stdin(str_n_q)
    char_list = get_char_list(n)

    # 処理スタート
    answer_list: List[str] = []
    while len(char_list) != 0:
        v = char_list.pop(0)
        answer_list = insert_value(v, answer_list, ask)

    return f"! {''.join(answer_list)}"
    # print(f"count ask is {count_ask}")


if __name__ == '__main__':
    # 標準入力から "N Q" を取得
    stdin_n_q = input()
    print(get_answer(stdin_n_q), flush=True)
