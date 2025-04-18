import heapq as hq

N = int(input())

h = []

for _ in range(N):
    dday, score = map(int, input().split())
    hq.heappush(h, (-score, dday))

schedule = [False] * 1000
total = 0

for _ in range(N):
    score, dday = hq.heappop(h)
    score = -score
    dday -= 1

    while dday > -1 and schedule[dday]:
        dday -= 1

    if dday > -1:
        schedule[dday] = True
        total += score

print(total)