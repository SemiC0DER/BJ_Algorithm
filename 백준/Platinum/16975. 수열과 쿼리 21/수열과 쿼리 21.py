#1275 구간 합 구하기 2

class SegmentTree():
    def __init__(self, array):
        self.array = array
        self.tree = [0] * (4 * len(array))
        self.lazy = [0] * (4 * len(array))
        self.setTree(1, 0, len(array) - 1)

    def setTree(self, index, start, end):
        if start == end:
            self.tree[index] = self.array[start]
            return self.tree[index]

        mid = (start + end) // 2
        self.setTree(index * 2, start, mid)
        self.setTree(index * 2 + 1, mid + 1, end)

    def lazy_replace(self, index, start, end):
        self.tree[index] += self.lazy[index] * (end - start + 1)
        if start < end:
            self.lazy[index * 2] += self.lazy[index]
            self.lazy[index * 2 + 1] += self.lazy[index]
        self.lazy[index] = 0

    def replace(self, index, start, end, left, right, diff):
        self.lazy_replace(index, start, end)
        if right < start or end < left:
            return 

        if left <= start and end <= right:
            self.lazy[index] += diff
            self.lazy_replace(index, start, end)
            return

        if self.lazy[index] != 0:
            self.lazy[index*2] += self.lazy[index]
            self.lazy[index * 2 + 1] = self.lazy[index]
            self.lazy[index] = 0
        mid = (start + end) // 2
        self.replace(index * 2, start, mid, left, right, diff)
        self.replace(index * 2 + 1, mid + 1, end, left, right, diff)
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def getTree(self, index, start, end, target):
        self.lazy_replace(index, start, end)
        if target == start == end:
            return self.tree[index]
        if target < start or end < target:
            return 0

        mid = (start + end) // 2
        if target <= mid:
            return self.getTree(index * 2, start, mid, target)
        else:
            return self.getTree(index * 2 + 1, mid + 1, end, target)

N = int(input())
array = list(map(int, input().split()))
st = SegmentTree(array)
M = int(input())
for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        st.replace(1, 0, N - 1, command[1] - 1, command[2] - 1, command[3])
    else:
        print(st.getTree(1, 0, N - 1, command[1] - 1))