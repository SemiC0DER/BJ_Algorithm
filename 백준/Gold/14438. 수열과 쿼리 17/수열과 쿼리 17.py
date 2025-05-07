#수열과 쿼리 17
import sys
input = sys.stdin.readline
class SegmentTree():
    def __init__(self, a):
        self.array = a
        self.tree= [None] * (len(a) * 4)
        self.setTree(1, 0, len(a) - 1)

    def setTree(self, node, start, end):
        if start == end:
            self.tree[node] = self.array[start]
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = min(self.setTree(node * 2, start, mid), self.setTree(node * 2 + 1, mid + 1, end))
        return self.tree[node]

    def getTree(self, node, start, end, left, right):
        if left <= start and end <= right:
            return self.tree[node]

        if right < start or end < left:
            return 10 ** 9

        mid = (start + end) // 2
        return min(self.getTree(node * 2, start, mid, left, right), self.getTree(node * 2 + 1, mid + 1, end, left, right))

    def replace(self, node, start, end, target):
        if start == end == target:
            self.tree[node] = self.array[target]
            return self.tree[node]
        
        if start == end:
            return self.tree[node]

        if target < start or end < target:
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = min(self.replace(node * 2, start, mid, target), self.replace(node * 2 + 1, mid + 1, end, target))
        return self.tree[node]

n = int(input())
a = list(map(int, input().split()))
st = SegmentTree(a)
m = int(input())

for _ in range(m):
    c, i, j = map(int, input().split())
    if c == 1:
        st.array[i - 1] = j
        st.replace(1, 0, n - 1, i - 1)
    else:
        print(st.getTree(1, 0, n - 1, i - 1, j - 1))