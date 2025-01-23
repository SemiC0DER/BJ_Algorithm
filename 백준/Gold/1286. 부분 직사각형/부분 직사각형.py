#1286 부분 직사각형

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
alphabet = [0] * 26

def countChar(x, y):
    return (x + 1) * (y + 1) * (2 * N - x) * (2 * M - y)

for i in range(2 * N):
    for j in range (2 * M):
        alphabet[ord(lst[i % N][j % M]) - 65] += countChar(i, j)

print(*alphabet, sep = '\n')