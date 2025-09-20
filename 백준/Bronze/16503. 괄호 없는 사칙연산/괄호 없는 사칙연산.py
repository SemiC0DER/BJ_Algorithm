a, o1, b, o2, c = input().split()

def op(x, o, y):
    x, y = int(x), int(y)
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    else:
        sign = -1 if (x < 0) ^ (y < 0) else 1
        return sign * (abs(x) // abs(y))

res1 = op(op(a, o1, b), o2, c)
res2 = op(a, o1, op(b, o2, c)) 

ans = sorted([res1, res2])
print(ans[0])
print(ans[1])
