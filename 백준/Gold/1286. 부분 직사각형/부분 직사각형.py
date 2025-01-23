#1286 부분 직사각형

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
alphabet = [0] * 26

def countChar(x, y):
    return x * y * (1 + 2 * N - x) * (1 + 2 * M - y)

for i in range(N):
    for j in range(M):
        x = i + 1
        y = j + 1
        alphabet[ord(lst[i][j]) - 65] += countChar(x, y) + countChar(N + x, y) + countChar(x, M + y) + countChar(N + x, M + y)

print(*alphabet, sep = '\n')