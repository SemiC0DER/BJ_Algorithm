n = int(input())
s = input()
count = 0
ana = []
for i in range(n):
    if s[i] == 'A':
        ana.append(s[i])
        if ana[-3:] == ['A', 'N', 'A']:
            count += 1
    elif s[i] == 'N':
        ana.append(s[i])

print(count)