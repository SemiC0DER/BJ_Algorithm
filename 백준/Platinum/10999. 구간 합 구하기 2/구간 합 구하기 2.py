#1275 구간 합 구하기 2

class SegmentTree():
    def __init__(self, array):
        self.array = array
        self.tree = [None] * (4 * len(array))
        self.lazy = [0] * (4 * len(array))
        self.setTree(1, 0, len(array) - 1)

    def setTree(self, index, start, end):
        if start == end:
            self.tree[index] = self.array[start]
            return self.tree[index]

        mid = (start + end) // 2
        self.tree[index] = self.setTree(index * 2, start, mid) + self.setTree(index * 2 + 1, mid + 1, end)
        return self.tree[index]

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

        mid = (start + end) // 2
        self.replace(index * 2, start, mid, left, right, diff)
        self.replace(index * 2 + 1, mid + 1, end, left, right, diff)
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def getTree(self, index, start, end, left, right):
        self.lazy_replace(index, start, end)
        if left <= start and end <= right:
            return self.tree[index]
        
        if right < start or end < left:
            return 0

        mid = (start + end) // 2
        return self.getTree(index * 2, start, mid, left, right) + self.getTree(index * 2 + 1, mid + 1, end, left, right)

N, M, K = map(int, input().split())
array = [int(input()) for _ in range(N)]
st = SegmentTree(array)

for _ in range(M + K):
    command = list(map(int, input().split()))
    if command[0] == 1:
        st.replace(1, 0, N - 1, command[1] - 1, command[2] - 1, command[3])
    else:
        print(st.getTree(1, 0, N - 1, command[1] - 1, command[2] - 1))