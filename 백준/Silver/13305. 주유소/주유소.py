N = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))[:-1]
stack = []
for _ in range(N - 1):
    dist = road.pop()
    gas = city.pop()
    while stack and stack[-1][0] > gas:
        dist += stack[-1][1]
        stack.pop()
    stack.append([gas, dist])

ans = 0
while stack:
    track = stack.pop()
    ans += track[0] * track[1]
print(ans)