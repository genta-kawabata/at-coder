# -*- coding: utf-8 -*-

MAX = 1e10
MIN = -MAX


def get_answer(A, B, W, count):
    if count == 1:
        if A <= W <= B:
            min = 1
            max = 1
            return min, max, True
    else:
        rec = get_answer(A, B, W - )



    pass



if __name__ == "__main__":
    A, B, W = map(int, input().split())

    W *= 1000

    min_value = 1001
    max_value = -1
    flg = False


    min_value = get_min(A, B, W)




    min_count = 0
    for i in range(1, 10000, 1):
        min_i = get_min(A, B, W, i)
        min_value = min(min_value, min_i)


        min = min(min_value, get_min())


        if W // i == 0:
            min_count = i
        else:







    flg_min = False
    for i in range(1, 10000, 1):
        if A <= W // i <= B:
            flg = True
            min_value = min(min_value, i)
            max_value = max(max_value, i)
    if flg:
        print(f"{min_value} {max_value}")
    else:
        print("UNSATISFIABLE")












    # flg = True
    # if W % A == 0:
    #     max_value = W // A
    # elif (W / A) >= 1:
    #     max_value = W // A
    # else:
    #     flg = False
    
    # if W % B == 0:
    #     min_value = W // B
    # elif (W / B) >= 1:
    #     min_value = W // B + 1
    # else:
    #     flg = False


    # if flg:
    #     print(f"{min_value} {max_value}")
    # else:
    #     print("UNSATISFIABLE")
