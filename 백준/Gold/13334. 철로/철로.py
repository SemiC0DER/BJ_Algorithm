#13334 철로
import heapq

n = int(input())
dist = sorted([sorted(list(map(int, input().split()))) for _ in range(n)], key = lambda x: (x[1], x[0]))
d = int(input())

heap = []
count = 0

for i in dist:
    start, end = i[0], i[1]
    if end - start > d:
        continue

    heapq.heappush(heap, start)
    
    while heap and end - d > heap[0]:
        heapq.heappop(heap)

    count = max(count, len(heap))

print(count)    