N = int(input())
MOD = 10007
dp = [1] * 10
for i in range(1, N):
    new_dp = [0] * 10
    new_dp[0] = 1
    for j in range(1, 10):
        new_dp[j] = sum(dp[:j+1]) % MOD
    dp = new_dp[:]
print(sum(dp) % MOD)