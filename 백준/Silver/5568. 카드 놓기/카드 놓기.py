from itertools import permutations

n = int(input())
k = int(input())
num = [input() for _ in range(n)]

sol = set()

for p in permutations(num, k):
    sol.add(''.join(p))

print(len(sol))
