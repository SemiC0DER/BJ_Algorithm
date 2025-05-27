import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
parent = list(range(N + 1))
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key = lambda x: x[2])

def union(a, b):
    a = getParent(a)
    b = getParent(b)

    if a == b:
        return False

    if a > b: a, b = b, a
    parent[b] = a
    return True

def getParent(a):
    if a == parent[a]:
        return a

    parent[a] = getParent(parent[a])
    return parent[a]

ans = 0
max_edge = 0
for i, j, cost in edges:
    if union(i, j):
        ans += cost
        max_edge = cost
print(ans - max_edge)