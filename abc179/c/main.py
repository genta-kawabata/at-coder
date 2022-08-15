def get_answer_kawa(n: int):

    counter = 0
    for a in range(1, n, 1):
        for b in range(1, n + 1, 1):
            c = n - a * b
            if c > 0:
                counter += 1
            else:
                break

    return counter


def get_answer_example(n: int):

    counter = 0
    for a in range(1, n, 1):
        counter += (n - 1) // a

    return counter


if __name__ == "__main__":
    N = int(input())
    print(get_answer_example(N))
