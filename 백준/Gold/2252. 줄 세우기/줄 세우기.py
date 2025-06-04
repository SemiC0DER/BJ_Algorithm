from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
position = [0] * (N + 1)
direction = [[] for _ in range(N + 1)]

for _ in range(M):
    front, behind = map(int, input().split())
    position[behind] += 1
    direction[front].append(behind)

q = deque()
for i in range(1, N + 1):
    if position[i] == 0:
        q.append(i)

ans = []
while q:
    finished = q.popleft()
    ans.append(finished)
    
    for next in direction[finished]:
        position[next] -= 1

        if position[next] == 0:
            q.append(next)
print(*ans)