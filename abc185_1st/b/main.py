def proc_stdin():
    _n, _m, _t = [int(x) for x in input().split(" ")]

    _list_a = []
    _list_b = []
    for i in range(_m):
        _a, _b = [int(x) for x in input().split(" ")]
        _list_a.append(_a)
        _list_b.append(_b)

    return _n, _m, _t, _list_a, _list_b


def charge(_crr_battery, _max_limit, _period):
    _crr_battery += _period
    if _crr_battery >= _max_limit:
        _crr_battery = _max_limit
    return _crr_battery


def discharge(_crr_battery, _period):
    _crr_battery -= _period
    return _crr_battery


def get_answer(_n, _m, _t, _list_a, _list_b):
    _crr_battery = _n
    _crr_time = 0

    for i in range(_m):
        # discharge
        period = _list_a[i] - _crr_time
        _crr_battery = discharge(_crr_battery, period)
        if _crr_battery <= 0:
            return "No"
        _crr_time += period

        # charge
        period = _list_b[i] - _list_a[i]
        _crr_battery = charge(_crr_battery, _n, period)
        _crr_time += period

    # discharge
    period = _t - _crr_time
    _crr_battery = discharge(_crr_battery, period)
    if _crr_battery <= 0:
        return "No"

    return "Yes"


if __name__ == '__main__':
    n, m, t, list_a, list_b = proc_stdin()

    print(get_answer(n, m, t, list_a, list_b))
