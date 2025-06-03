change = 1000 - int(input())
coinlist = [500, 100, 50, 10, 5, 1]
ans = 0
for i in range(6):
    ans += change // coinlist[i]
    change %= coinlist[i]
print(ans)