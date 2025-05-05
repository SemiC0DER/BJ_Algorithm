#2243 사탕상자
import sys
input = sys.stdin.readline

class CandyBox():
    def __init__(self):
        self.tree = [0] * 4 * 10**6
        
    def putCandy(self, start, end, node, taste, count):
        self.tree[node] += count

        if start == end:
            return

        mid = (start + end)//2

        if taste <= mid:
            self.putCandy(start, mid, node * 2, taste, count)
        else:
            self.putCandy(mid + 1, end, node * 2 + 1, taste, count)

    def getCandy(self, start, end, node, rank):
        self.tree[node] -= 1

        if start == end:
            return start

        mid = (start + end) // 2

        if self.tree[node * 2] >= rank:
            return self.getCandy(start, mid, node*2, rank)
        else:
            return self.getCandy(mid + 1, end, node*2+1, rank - self.tree[node*2])

n = int(input())
box = CandyBox()
for _ in range(n):
    line = list(map(int, input().split()))
    if len(line) == 2:
        rank = line[1]
        print(box.getCandy(1, 10 ** 6, 1, rank))
    else:
        taste, count = line[1], line[2]
        box.putCandy(1, 10 ** 6, 1, taste, count)