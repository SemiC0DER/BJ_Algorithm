N, K = map(int, input().split())
MOD = 10007


fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD


def modinv(x):
    return pow(x, MOD - 2, MOD)

denom = (fact[K] * fact[N - K]) % MOD
result = (fact[N] * modinv(denom)) % MOD

print(result)
