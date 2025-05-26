N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(N - 1, -1, -1):
    add = 0
    for j in range(i + 1, N):
        if A[i] > A[j]:
            add = max(add, dp[j])
    dp[i] += add
print(max(dp))