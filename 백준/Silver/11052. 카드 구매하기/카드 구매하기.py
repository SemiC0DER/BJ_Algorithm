N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(1, N + 1):
    new_dp = [0] * (N + 1)
    for j in range(i):
        new_dp[j] = dp[j]
    for j in range(i, N + 1):
        new_dp[j] = max(dp[j], new_dp[j - i] + P[i])
    dp = new_dp[:]
print(dp[N])