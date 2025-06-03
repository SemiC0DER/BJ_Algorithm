import sys
input = sys.stdin.readline
T = int(input())
coinlist = [25, 10, 5, 1]
for _ in range(T):
    change = int(input())
    ans = []
    for i in range(4):
        ans.append(change // coinlist[i])
        change %= coinlist[i]
    print(*ans)