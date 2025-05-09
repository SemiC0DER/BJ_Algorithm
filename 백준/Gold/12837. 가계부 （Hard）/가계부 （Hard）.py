#12837 가계부
import sys
input = sys.stdin.readline
def getTree(left, right):
    def _getTree(node, start, end):
        if left <= start and end <= right:
            return tree[node]
        
        if right < start or end < left:
            return 0

        mid = (start + end) // 2
        return _getTree(node * 2, start, mid) + _getTree(node * 2 + 1, mid + 1, end)
    
    return _getTree(1, 0, n - 1)

def replace(target, value):
    def _replace(node, start, end):
        if start == end == target:
            tree[node] += value
            return
        tree[node] += value
        mid = (start + end) // 2
        if target <= mid:
            _replace(node * 2, start, mid)
        else:
            _replace(node * 2 + 1, mid + 1, end)

    _replace(1, 0, n - 1)
        
n, q = map(int, input().split())
tree = [0] * (n * 4)
array = [0] * n
for _ in range(q):
    c, i, j = map(int, input().split())
    if c == 1:
        replace(i - 1, j)
        array[i - 1] += j
    else:
        print(getTree(i - 1, j - 1))