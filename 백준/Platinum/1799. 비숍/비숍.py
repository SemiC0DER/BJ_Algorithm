#1799 비숍

def track(row, col, count, color):
    if col >= N:
        row += 1
        if col % 2 == 0:
            col = 1
        else:
            col = 0

    if row >= N:
        ans[color] = max(ans[color], count)
        return

    if chess[row][col] and not l[col - row + N - 1] and not r[row + col]:
        l[col - row + N - 1], r[row + col] = True, True
        track(row, col + 2, count + 1, color)
        l[col - row + N - 1], r[row + col] = False, False
    
    track(row, col + 2, count, color)

N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]
l = [False] * 20
r = [False] * 20
track(0, 0, 0, 0)
track(0, 1, 0, 1)
print(sum(ans))