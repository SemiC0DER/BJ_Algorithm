#1931 회의실 배정

N = int(input())

meetings = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x : (x[0], x[1]))
reservation = 1
last = meetings[0][1]
6 
for start, end in meetings[1:]:
    
    if start >= last:
        reservation += 1
        last = end
    
    elif end < last:
        last = end

print(reservation)