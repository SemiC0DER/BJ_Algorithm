#1946 신입 사원
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    new = sorted([list(map(int, input().split())) for _ in range(N)])
    ans = 1
    maxi = new[0][1]
    for i in range(1, N):
        if maxi > new[i][1]:
            ans += 1
            maxi = new[i][1]
        
    print(ans)