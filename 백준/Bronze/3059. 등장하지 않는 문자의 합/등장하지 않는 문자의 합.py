n = int(input())
alpahbet = set(range(65, 91))
for _ in range(n):
    data = set(list(map(lambda x: ord(x), list(input()))))
    print(sum(alpahbet - data))