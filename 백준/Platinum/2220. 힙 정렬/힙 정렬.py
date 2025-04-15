#2220 힙 정렬

N = int(input())
hq = [None, 1]
swap = 0

def swapHeap(n):
    current = len(hq) - 1

    while current != 1:
        parent = current // 2
        hq[current], hq[parent] = hq[parent], hq[current]
        current = parent

    hq.append(n)
    hq[1], hq[-1] = hq[-1], hq[1]

for i in range(2, N + 1):
    swapHeap(i)

print(*hq[1:])