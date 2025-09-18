import sys
A = list(map(int, sys.stdin.read().split()))
s = sum(A)
print(s // 60, s % 60, sep = '\n')