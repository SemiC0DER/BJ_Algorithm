#1826 연료 채우기
from heapq import heappush, heappop
N = int(input())

station = sorted([list(map(int, input().split())) for _ in range(N)])
L, P = map(int, input().split())
station.append([L, 0])
cur_gas = P
heap = []
ans = 0

for x in station:
    st_loc, st_gas = x[0], x[1]
    if cur_gas >= L:
        break
    while cur_gas < st_loc and heap:
        cur_gas += -heappop(heap)
        ans += 1
    if cur_gas < st_loc:
        break
    heappush(heap, -st_gas)

print(ans if cur_gas >= L else -1)