t = int(input())
for _ in range(t):
    n = int(input())
    dot = list(map(int, input().split()))
    dot_set = set(dot)
    sol = set()
    for i in range(n):
        for j in range(i + 1, n):
            a, b = min(dot[i], dot[j]), max(dot[i], dot[j])
            diff = b - a
            if b + diff in dot_set:
                sol.add(f"{a} {b} {b + diff}")
            if a - diff in dot_set:
                sol.add(f"{a - diff} {a} {b}")
    print(len(sol))