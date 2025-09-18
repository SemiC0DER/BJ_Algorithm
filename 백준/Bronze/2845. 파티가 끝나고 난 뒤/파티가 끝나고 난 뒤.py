a, b = map(int, input().split())
c = a * b
paper = list(map(lambda x: int(x) - c, input().split()))
print(*paper)
