N = int(input())
a = list(map(int, input().split()))
streak = 1
score = 0
for i in range(N):
    if a[i] == 1:
        score += streak
        streak += 1
    else:
        streak = 1
        
print(score)