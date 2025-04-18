import heapq

n, m = map(int, input().split())

answer = []
graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n+1)]
queue = []


for i in range(m): #n
    first, second = map(int, input().split())
    graph[first].append(second)
    inDegree[second] += 1

for i in range(1, n + 1): #n
    if inDegree[i] == 0:
        heapq.heappush(queue, i)

while queue: #n2
    tmp = heapq.heappop(queue) #logn
    answer.append(tmp)
    for i in graph[tmp]: #n
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(queue, i)


print(" ".join(map(str, answer)))