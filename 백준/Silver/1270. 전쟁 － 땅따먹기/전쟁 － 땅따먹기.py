#전쟁 - 땅따먹기

n = int(input())
for _ in range(n):
    land = list(map(int, input().split()))
    soldier = land[0]
    throne = soldier // 2 + 1
    d = {}
    peace = 'SYJKGW'
    for i in range(1, len(land)):
        if land[i] in d:
            d[land[i]] += 1
        else:
            d[land[i]] = 1

        if d[land[i]] >= throne:
            peace = land[i]
    print(peace)