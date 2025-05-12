import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(0, n + 1))
def getParent(child):
    if parent[child] == child:
        return child

    parent[child] = getParent(parent[child])
    return parent[child]

def parentUnion(a, b):
    aP = getParent(a)
    bP = getParent(b)

    if aP < bP:
        parent[bP] = aP
    else:
        parent[aP] = bP

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        parentUnion(a, b)
    else:
        if getParent(a) == getParent(b):
            print("YES")
        else:
            print("NO")