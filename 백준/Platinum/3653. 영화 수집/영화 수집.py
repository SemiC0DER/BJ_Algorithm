#3653 영화 수집

class Movie():
    def __init__(self, n, m):
        self.array_len = n + m
        self.top = n - 1
        self.loc = [0] + [i for i in range(n - 1, -1, -1)]
        self.tree = [0] * (4 * (n + m))
        self.ans = []

    def watch(self, target):
        tg_loc = self.loc[target]
        left, right = tg_loc + 1, self.top

        def _get(node, start, end):
            if left <= start and end <= right:
                return self.tree[node]

            if right < start or end < left:
                return 0

            mid = (start + end) // 2
            return _get(node * 2, start, mid) + _get(node * 2 + 1, mid + 1, end)

        stacked = self.top - tg_loc - _get(1, 0, self.array_len - 1)
        self.ans.append(stacked)
        self.top += 1
        self.loc[target] = self.top

        def _out(node, start, end):
            if start == end:
                self.tree[node] += 1
                return
            
            self.tree[node] += 1
            mid = (start + end) // 2
            if tg_loc <= mid:
                _out(node * 2, start, mid)
            else:
                _out(node * 2 + 1, mid + 1, end)

        _out(1, 0, self.array_len - 1)
            


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    movie = Movie(n, m)
    for m_num in map(int, input().split()):
        movie.watch(m_num)
    print(*movie.ans)