n = int(input())
v = list(map(int, input().split()))
v.sort(reverse=True)

pSum = [0] * (n + 2)

for i in range(n):
    end = i + v[i]
    if end > n:
        pSum[i] += 1
        pSum[0] += 1
        pSum[(end % n)] -= 1
        pSum[n] -= 1
    else:
        pSum[i] += 1
        pSum[end] -= 1

for i in range(1, n):
    pSum[i] += pSum[i - 1]

cnt = sum(1 for i in range(n) if pSum[i] > 0)
print(cnt)
