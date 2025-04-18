#컵라면 
import heapq

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort(key = lambda x: (x[0], -x[1]))
hq = []
time, result = 1, 0
for deadline, ramen in data:
    if time <= deadline:
        result += ramen
        heapq.heappush(hq, (ramen, time))
        time += 1
    else:
        if hq:
            min_ramen = hq[0]
            if min_ramen[0] < ramen:
                result += (ramen - min_ramen[0])
                heapq.heappushpop(hq, (ramen, min_ramen[1]))
print(result)