BIT = 1 << 10
NUM = 10
MOD = 1000000000
N = int(input())

dp = [[[0] * BIT for _ in range(NUM)] for _ in range(N + 1)]
#dp[i][j][k] i:자리수 j:마지막숫자: k:사용된 숫자들의 비트

for j in range(1, NUM):
    dp[1][j][1 << j] = 1

for i in range(1, N):
    for j in range(NUM):
        for k in range(BIT):
            if j > 0:
                next = k | 1 << (j - 1)
                dp[i + 1][j - 1][next] += dp[i][j][k]
                dp[i + 1][j - 1][next] %= MOD
            if j < 9:
                next = k | 1 << (j + 1)
                dp[i + 1][j + 1][next] += dp[i][j][k]
                dp[i + 1][j + 1][next] %= MOD

res = 0
for i in range(NUM):
    res += dp[N][i][BIT-1]
    res %= MOD

print(res)                