a, b = map(int, input().split())
ans = 1
while True:
    if b == a:
        print(ans)
        break
    
    if b % 2 == 0:
        b //= 2
        ans += 1
        continue
    
    if b > 10 and b % 10 == 1:
        b //= 10
        ans += 1
        continue
    print(-1)
    break