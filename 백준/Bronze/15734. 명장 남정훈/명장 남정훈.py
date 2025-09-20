l, r, a = map(int, input().split())
diff = abs(l - r)
if a - diff < 0:
    print(l + r + a + a - diff)
else:
    print(l + r + a - (a - diff) % 2)