N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse = True)
ans = 0
for i in range(N):
    ans = max(ans, (1 + i) * ropes[i])
print(ans)