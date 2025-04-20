#2696 중앙값 구하기

import heapq

T = int(input())
for _ in range(T):
    M = int(input())
    min_heap = []
    max_heap = []
    ans = []
    idx = True
    for _ in range((M - 1) // 10 + 1):
        for num in map(int, input().split()):
            if not min_heap or num < min_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

            if len(min_heap) >= len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            elif len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            if idx:
                idx = False
                ans.append(-max_heap[0])
            else:
                idx = True
    
    print(len(ans))
    for i in range(0, len(ans), 10):
        print(*ans[i:i+10])