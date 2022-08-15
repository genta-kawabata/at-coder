import math


def get_diff_list(n, in_list: list) -> list:
    in_list.append(0)
    in_list.append(n + 1)
    in_list.sort()

    tail = 0
    diff_list = []
    for v in in_list:
        d = v - tail - 1
        if d > 0:
            diff_list.append(d)
        tail = v

    return diff_list


def get_answer(n, m, list_a):
    if n == len(list_a):
        return 0

    list_a.sort()
    diff_list = get_diff_list(n, list_a)

    count = 0
    k = min(diff_list)

    for diff in diff_list:
        count += math.ceil(diff / k)

    return count


if __name__ == '__main__':
    _n, _m = [int(v) for v in input().split(" ")]
    if _m != 0:
        _list_a = [int(v) for v in input().split(" ")]
    else:
        _list_a = []
    print(get_answer(_n, _m, _list_a))
