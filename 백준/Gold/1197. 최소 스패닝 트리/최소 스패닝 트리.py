#1197 최소 스패닝 트리
import sys
sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().rstrip()
def getParent(vertex):
    if parent[vertex] == vertex:
        return vertex

    parent[vertex] = getParent(parent[vertex])
    return parent[vertex]

def union(a, b):
    a = getParent(a)
    b = getParent(b)

    if a == b:
        return False

    if a > b: a, b = b, a

    parent[b] = a
    return True

v, e = map(int,  input().split())
parent = list(range(v + 1))
edges = []
for _ in range(e):
    a, b, c = map(int , input().split())
    edges.append((c, a, b))

edge_count = 0
ans = 0

for val, start, end in sorted(edges):
    if union(start, end):
        ans += val
        edge_count += 1
        if edge_count == v - 1:
            print(ans)
            break