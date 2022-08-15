# -*- coding: utf-8 -*-

from typing import List


def get_cumulative_sum_sequential(numbers):
    result = [0]
    for number in numbers:
        result.append(result[-1] + number)
    return result

def get_answer(list_A: List[int]):

    # sorted_list_A = list_A.copy()
    # sorted_list_A.sort()

        


    # max = -1
    # num_value = 1
    # while num_value <= len(list_A):
    #     j = 0
    #     while j + num_value <= len(list_A):

    #         new_list = list_A[j:j + num_value]
    #         x = min(new_list)
    #         sum = x * num_value
    #         if sum > max:
    #             max = sum
    #         j += 1
    #     num_value += 1
    # return max


    max_sum = -1
    for l in range(len(list_A)):
        x = list_A[l]
        for r in range(l, len(list_A), 1):
            x = min(x, list_A[r])
            sum = x * (r - l + 1)
            # max_sum = max(max_sum, sum)
            # if sum > max_sum:
            #     max_sum = sum
            max_sum = sum if sum > max_sum else max_sum
    
    return max_sum


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N = int(input())
    _l_A = list(map(int, input().split()))

    print(get_answer(_l_A))
