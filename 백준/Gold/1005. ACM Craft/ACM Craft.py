#1005 ACM Craft
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def sol():
    n, k = map(int, input().split())
    topos = [0] * (n + 1)
    start_time = [0] * (n + 1)
    direction = [[] for _ in range(n + 1)]
    ready_q = set()

    time_cost = [None] + list(map(int, input().split()))

    for _ in range(k):
        x, y = map(int, input().split())
        topos[y] += 1
        direction[x].append(y)

    victory = int(input())
    q = []
    for i in range(1, n + 1):
        if topos[i] == 0:
            q.append(i)
            ready_q.add(i)

    q = deque(q)

    while q:
        finished = q.popleft()
        finish_time = start_time[finished] + time_cost[finished]
        if finished == victory:
            return finish_time

        for next in direction[finished]:
            topos[next] -= 1
            start_time[next] = max(start_time[next], finish_time)
            if topos[next] == 0 and not next in ready_q:
                q.append(next)
                ready_q.add(next)

    return finish_time

T = int(input())
for _ in range(T):
    print(sol())