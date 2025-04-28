#13414 수강신청
import sys
input = sys.stdin.readline

K, L = map(int, input().split())
d = {}
priority = 0

for _ in range(L):
    num = input().rstrip()
    d[num] = priority
    priority += 1

a = sorted(d.keys(), key = lambda x: d[x])[:K]
print(*a, sep = '\n')