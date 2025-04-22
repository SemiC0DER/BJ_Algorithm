import sys
import heapq
input = sys.stdin.readline

N, k = map(int, input().split())

casher_list = []
empty_casher_list = list(range(k))
heapq.heapify(empty_casher_list)

idx, t = 1, 0
answer = 0

for _ in range(N):
    id, w = map(int, input().split())
    if len(casher_list) == k:
        t = casher_list[0][0]
        while casher_list and casher_list[0][0] == t:
            _, prev_casher, prev_id = heapq.heappop(casher_list)
            heapq.heappush(empty_casher_list, -prev_casher)
            answer += idx * prev_id
            idx += 1
    heapq.heappush(casher_list, (t + w, -heapq.heappop(empty_casher_list), id))

while casher_list:
    _, _, prev_id = heapq.heappop(casher_list)
    answer += idx * prev_id
    idx += 1

print(answer)
