#13537 수열과 쿼리 1
from bisect import bisect_right
import sys
input = lambda: sys.stdin.readline().rstrip()

class SegmentTree():
    def __init__(self, a):
        self.array = a
        self.tree = [None] * (len(a) * 4)
        self.setTree(1, 0, len(a) - 1)
    
    def setTree(self, node, start, end):
        if start == end:
            self.tree[node] = [self.array[start]]
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = sorted(self.setTree(node * 2, start, mid) + self.setTree(node * 2 + 1, mid + 1, end))
        return self.tree[node]

    def getTree(self, left, right, target):
        def _getTree(node, start, end):
            if left <= start and end <= right:
                idx = bisect_right(self.tree[node], target)
                return len(self.tree[node]) - idx

            if right < start or end < left:
                return 0

            mid = (start + end) // 2
            return _getTree(node * 2, start, mid) + _getTree(node * 2 + 1, mid + 1, end)
        return _getTree(1, 0, len(self.array) - 1)

N = int(input())
array = list(map(int, input().split())) 
st = SegmentTree(array)
M = int(input())
for _ in range(M):
    i, j, k = map(int, input().split())
    print(st.getTree(i - 1, j - 1, k))