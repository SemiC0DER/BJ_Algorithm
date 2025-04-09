#25381

s = input()
ans = 0
a = 0
b = 0
b_total = 0

for i in range(len(s)):
    if s[i] == 'A':
        a += 1
    elif s[i] == 'B':
        b += 1
        b_total += 1
        if a:
            ans += 1
            a -= 1
    else:
        if b:
            ans += 1
            b -= 1

print(min(ans, b_total))