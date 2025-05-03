#14428 수열과 쿼리 16

class SegmentTree():
    def __init__(self, array):
        self.array = array
        self.tree = [None] * (4 * len(array))
        self.setTree(1, 0, len(array) - 1)

    def setTree(self, index, start, end):
        if start == end:
            self.tree[index] = start
            return self.tree[index]

        mid = (start + end) // 2
        child1 = self.setTree(index * 2, start, mid)
        child2 = self.setTree(index * 2 + 1, mid + 1, end)
        if self.array[child1] == self.array[child2]:
            self.tree[index] =  min(child1, child2)
        else:
            self.tree[index] = child1 if self.array[child1] < self.array[child2] else child2
            
        return self.tree[index]

    def replace(self, index, start, end, target):
        if start == end == target:
            return self.tree[index]

        if target < start or end < target:
            return self.tree[index]

        mid = (start + end) // 2
        child1 = self.replace(index * 2, start, mid, target)
        child2 = self.replace(index * 2 + 1, mid + 1, end, target)
        if self.array[child1] == self.array[child2]:
            self.tree[index] =  min(child1, child2)
        else:
            self.tree[index] = child1 if self.array[child1] < self.array[child2] else child2
        return self.tree[index]

    def getTree(self, index, start, end, left, right):
        if left <= start and end <= right:
            return self.tree[index]

        if right < start or end < left:
            return None

        mid = (start + end) // 2
        child1 = self.getTree(index * 2, start, mid, left, right)
        child2 = self.getTree(index * 2 + 1, mid + 1, end, left, right)
        if child1 is None:
            return child2
        elif child2 is None:
            return child1
        else:
            if self.array[child1] == self.array[child2]:
                return min(child1, child2)
            else:
                return child1 if self.array[child1] < self.array[child2] else child2

N = int(input())
array = list(map(int, input().split()))
st = SegmentTree(array)
M = int(input())
for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        st.array[command[1] - 1] = command[2]
        st.replace(1, 0, N - 1, command[1] - 1)
    else:
        print(1 + st.getTree(1, 0, N - 1, command[1] - 1, command[2] - 1))