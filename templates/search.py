from typing import Any, List


def sequential(key: Any, arr: List[Any]) -> int:
    if key in arr:
        for i, v in enumerate(arr):
            if v == key:
                return i
    else:
        return -1


def binary_ordinary(key: Any, sorted_arr: List[Any]) -> int:
    """
    sorted_arr の中から key の値を探索しその index を返す。
    見つからなかった場合は -1 を返す
    key となる値が配列内に重複している場合は...
    """

    left: int = 0                       # index = 0 が条件を満たす（0以上が右側）こともあるので、初期値は -1
    right: int = len(sorted_arr) -1     # index = len - 1 が条件を満たさない（len-1以下が左側）こともあるので、初期値は len

    while (left <= right):
        mid: int = int(left + (right - left) / 2)
        # print(f"({left}, {mid}, {right})")
        if sorted_arr[mid] == key:
            return mid
        elif key < sorted_arr[mid]:
            right = mid - 1
        elif key > sorted_arr[mid]:
            left = mid + 1

    return -1


"""
汎用的な二分探索めぐる式二分探索
配列 a の index (正確には iterator) のうち key 以上となる最小の index を返す

返す index が持つ意味
・配列 a の中に値 key がなくても、key が a の中で何番目に小さいかわかる
・配列 a の中に値 key が複数あったとき、そのうちの最小の index を取って来れる
・発展テクとして std::upper_bound() も併用すれば、配列 a の中に値 key をもつものが何個あるかもわかる

ref https://qiita.com/drken/items/97e37dd6143e33a64c8c
"""
def binary_meguru(key: Any, sorted_arr: List[Any]) -> int:
    left = -1
    right = len(sorted_arr)

    while right - left > 1:
        mid: int = int(left + (right - left) / 2)

        if sorted_arr[mid] < key:
            left = mid
        else:
            right = mid

    if sorted_arr[right] == key:
        return right
    else:
        return -1
