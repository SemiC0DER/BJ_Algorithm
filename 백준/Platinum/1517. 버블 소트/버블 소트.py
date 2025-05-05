n = int(input())
a = list(map(int, input().split()))
idx_list = list(range(0, n))
idx_list.sort(key = lambda x: a[x])
tree = [0] * (4 * n)

def putNum(start, end, node, num):
    if start == end:
        tree[node] = 1
        return
    
    tree[node] += 1

    mid = (start + end) // 2

    if num <= mid:
        putNum(start, mid, node * 2, num)
    else:
        putNum(mid + 1, end, node * 2 + 1, num)

def getRange(start, end, node, left, right):
    if left <= start and end <= right:
        return tree[node]

    if right < start or end < left:
        return 0

    mid = (start + end) // 2
    return getRange(start, mid, node * 2, left, right) + getRange(mid + 1, end, node * 2 + 1, left, right)

count = 0
for i in range(n):
    count += getRange(0, n - 1, 1, idx_list[i] + 1, n - 1)
    putNum(0, n - 1, 1, idx_list[i])

print(count)