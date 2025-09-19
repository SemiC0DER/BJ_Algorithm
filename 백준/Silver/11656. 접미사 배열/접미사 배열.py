s = input()
a = sorted([s[i:] for i in range(len(s))])
print(*a, sep = '\n')