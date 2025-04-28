#22233 가희와 키워드

N, M = map(int, input().split())
keyword = set()

for _ in range(N):
    keyword.add(input().rstrip())

for _ in range(M):
    for word in input().rstrip().split(','):
        if word in keyword:
            keyword.discard(word)
    print(len(keyword))