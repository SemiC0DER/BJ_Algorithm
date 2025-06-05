#10162 전자레인지

button = [300, 60, 10]

T = int(input())
ans = []
for i in range(3):
    ans.append(T // button[i])
    T %= button[i]

print(*ans) if T == 0 else print(-1)