#4158 CD

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    print(len(set([input() for _ in range(N)]) & set([input() for _ in range(M)])))