import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for _ in range(N)]  # -1로 초기화

def dfs(x, visited):
    if visited == (1 << N) - 1:
        return graph[x][0] if graph[x][0] else float('inf')

    if dp[x][visited] != -1:
        return dp[x][visited]

    min_cost = float('inf')
    for i in range(N):
        if not graph[x][i] or visited & (1 << i):
            continue
        cost = dfs(i, visited | (1 << i)) + graph[x][i]
        min_cost = min(min_cost, cost)

    dp[x][visited] = min_cost
    return dp[x][visited]

result = dfs(0, 1)
print(result)
