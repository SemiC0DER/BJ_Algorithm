def locate(m, idx):
    num = 0
    i = idx
    while i > 0:
        num += fenwick[i]
        i -= i & -i

    i = idx
    while i <= n:
        fenwick[i] += 1
        i += i & -i

    return m - num

n = int(input())
fenwick = [0] * (n + 1)
loc = {}
count = 0

for index, a in enumerate(map(int, input().split())):
    loc[a] = index + 1

for index, b in enumerate(map(int, input().split())):
    count += locate(index, loc[b])

print(count)