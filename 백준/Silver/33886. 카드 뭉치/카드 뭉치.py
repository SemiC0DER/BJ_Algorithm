N = int(input())
cards = list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    dp[i] = dp[i + 1] + 1
    for j in range(2, cards[i] + 1):
        if i + j > N:
            continue
        dp[i] = min(dp[i], dp[i + j] + 1)
print(dp[0])