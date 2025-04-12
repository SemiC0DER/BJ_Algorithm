X = int(input())
n = 1

while (k := (X - n * (n + 1) // 2)) > 0:
    n += 1

here = n + k
there = n + 1 - here

print(f"{here}/{there}" if n % 2 == 0 else f"{there}/{here}")