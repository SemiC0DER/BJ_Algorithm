#1931 회의실 배정

N = int(input())

meetings = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x : (x[0], x[1]))
reservation = 1
last = meetings[0][1]
6 
for i in range(1, N):
    start, end = meetings[i][0], meetings[i][1]
    if start >= last:
        reservation += 1
        last = end
    
    elif end < last:
        last = end

print(reservation)