from heapq import *
K, N = map(int, input().split())
prime = list(map(int, input().split()))
hq = prime[:]
for _ in range(N):
    num = heappop(hq)
    for i in range(K):
        heappush(hq, num * prime[i])
        if num % prime[i] == 0:
            break
print(num)