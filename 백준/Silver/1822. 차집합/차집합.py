#1822 차집합

a, b = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

C = A - B
if C == 0:
    print(0)
else:
    print(len(C))
    print(*sorted(C))