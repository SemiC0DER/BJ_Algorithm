#33888
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N + 1)]
three_edges = []
four_edges = []
for _ in range(N + 3):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
for i in range(1, N + 1):
    if len(graph[i]) == 1:
        tail = i
        break

def jumppath(prev, node):
    visited.add(node)
    while len(graph[node]) == 2:
        for next in graph[node]:
            if next != prev:
                if next not in visited:
                    prev, node = node, next
                    visited.add(next)
                    break
                else:
                    return False
    return node

def bfs(start):
    visited.add(start)
    visited.update(graph[start])
    q = deque(graph[start])

    while q:
        node = q.popleft()
        if len(graph[node]) == 3:
            three_edges.append(node)
        elif len(graph[node]) == 4:
            four_edges.append(node)

        for next in graph[node]:
            if next not in visited:
                next = jumppath(node, next)
                if not next:
                    continue
                visited.add(next)
                q.append(next)

bfs(tail)
left, right, head = three_edges[0], three_edges[1], three_edges[2]
if left > right: right, left = left, right
bottom, center = four_edges[0], four_edges[1]
print(head, left, center, right, bottom, tail)