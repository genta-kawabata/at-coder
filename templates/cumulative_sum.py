def get_cumulative_sum_list(list_no):
    """forで累積和を求める。
    This method works.
    """
    result = [0]
    for number in list_no:
        result.append(result[-1] + number)
    return result

def get_cumulative_sum_list_mod(list_no, mod):
    """forで累積和を求める。 MOD 使用
    This method works.
    """
    result = [0]
    for number in list_no:
        sum = result[-1] + number
        if sum < 0:
            sum += mod
        sum %= mod
        result.append(sum)
    return result

def get_sum_from_cum_sum_list(cum_sum_list, start, stop):
    """
    元の配列 L_A の A_start + ... + A_{stop-1} を求める
    """
    return cum_sum_list[stop] - cum_sum_list[start]
