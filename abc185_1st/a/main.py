if __name__ == '__main__':

    std_line = input()

    ns = std_line.split(" ")

    int_ns = [int(x) for x in ns]
    print(min(int_ns))
