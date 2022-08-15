# -*- coding: utf-8 -*-


if __name__ == "__main__":
    S = input()

    for i, s in enumerate(S):
        if (i + 1) % 2 == 1:
            if s.isupper():
                print("No")
                quit()
        else:
            if s.islower():
                print("No")
                quit()
    
    print("Yes")

