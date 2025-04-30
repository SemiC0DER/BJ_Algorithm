n, m = map(int, input().split())
d = {}
for _ in range(n):
    _ = input()
    st_list = list(input().split())
    for student in st_list:
        if student in d:
            d[student] += 1
        else:
            d[student] = 1

count = 0
for value in d.values():
    if value >= m:
        count += 1

print(count)