#5676 음주 코딩

class SegmentTree():
    def __init__(self, a):
        self.array = a
        self.tree = [None] * (len(a) * 4)
        self.setTree(1, 0, len(a) - 1)

    def setTree(self, node, start, end):
        if start == end:
            self.tree[node] = self.array[start]
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = self.setTree(node * 2, start, mid) * self.setTree(node * 2 + 1, mid + 1, end)
        return self.tree[node]

    def replace(self, node, start, end, target, value):
        if start == target == end:
            self.tree[node] = value
            self.array[target] = value
            return self.tree[node]

        if target < start or end < target:
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = self.replace(node * 2, start, mid, target, value) * self.replace(node * 2 + 1, mid + 1, end, target, value)
        return self.tree[node]

    def getTree(self, node, start, end, left, right):
        if left <= start and end <= right:
            return self.tree[node]

        if right < start or end < left:
            return 1

        mid = (start + end) // 2
        return self.getTree(node * 2, start, mid, left, right) * self.getTree(node * 2 + 1, mid + 1, end, left, right)

while True:
    try:
        n, k = map(int, input().split())
        a = list(map(lambda x: 0 if x == '0' else (1 if int(x) > 0 else -1), input().split()))
        st = SegmentTree(a)

        ans = []
        for _ in range(k):
            c, i, j = input().split()
            i, j = int(i), int(j)
            if c == 'P':
                ans.append(st.getTree(1, 0, n - 1, i - 1, j - 1))
            else:
                if j != 0:
                    j = 1 if j > 0 else -1
                if st.array[i - 1]== j:
                    continue
                else:
                    st.replace(1, 0, n - 1, i - 1, j)

        ans = list(map(lambda x: '0' if x == 0 else ('+' if x > 0 else '-'), ans))
        print(*ans, sep = '')
    except:
        break