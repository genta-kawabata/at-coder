# answer = ((a0 + ... + aN)^2 - (a0^2 + ... + aN^2)) // 2
# answer = answer % MOD

MOD = int(1e9) + 7

def get_answer(n, l_a):
    S_A = sum(l_a)
    S2 = sum(map(lambda x: x * x, l_a))
    ans = ((S_A * S_A - S2) // 2) % MOD
    return ans


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    print(get_answer(N, A))
