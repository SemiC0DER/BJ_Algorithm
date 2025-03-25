#2048 Hello, 2048!
import sys
input = sys.stdin.readline

T = int(input())
m = [[0, 2, 2, 5],
     [0, 1, 3, 3],
     [0, 0, 2, 4],
     [0, 0, 0, 3]]
     
for i in range(T):
    l, r = map(int, input().split())
    if r >= 4:
        print(r)
    else:
        print(m[l][r])