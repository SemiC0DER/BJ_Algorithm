#32401 ANA는 회문이야

n = int(input())
s = input()
count = 0

for i in range(n):
    for j in range(i + 2, n):
        if s[i] == 'A' and s[j] == 'A' and s[i : j+1].count('N') == 1 and s[i: j+1].count('A') == 2:
            count += 1   

print(count)