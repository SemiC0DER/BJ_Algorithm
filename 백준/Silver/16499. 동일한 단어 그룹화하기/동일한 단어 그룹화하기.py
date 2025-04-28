n = int(input())
groups = set()

for _ in range(n):
    word = ''.join(sorted(input()))
    groups.add(word)

print(len(groups))
