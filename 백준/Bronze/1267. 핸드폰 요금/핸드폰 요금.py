N = int(input())
call = list(map(int, input().split()))
Y = 0
M = 0

for i in range(N):
    Y += call[i] // 30 * 10
    M += call[i] // 60 * 15
    if call[i] % 30 >= 0:
        Y += 10 
    if call[i] % 60 >= 0:
        M += 15 
    
if Y < M:
    print('Y', Y)
elif Y > M:
    print('M', M)
else:
    print('Y M', Y)