#14427 수열과 쿼리 15
import heapq

N = int(input())
A = [None] + list(map(int, input().split()))
heap = []

for i in range(1, N + 1):
    heapq.heappush(heap, [A[i], i])

M = int(input())

for _ in range(M):
    query = list(map(int, input().split()))

    if query[0] == 1:
        index, value = query[1], query[2]
        A[index] = value
        heapq.heappush(heap, [value, index])
    else:
        while A[heap[0][1]] != heap[0][0]:
            heapq.heappop(heap)
        print(heap[0][1])