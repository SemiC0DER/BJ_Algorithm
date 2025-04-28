n, m = map(int, input().split())
d = {}
for i in range(n):
    song = input().split()
    front = ''.join(song[2:5])
    if front in d:
        d[front].append(song[1])
    else:
        d[front] = [song[1]]

for i in range(m):
    front = ''.join(input().split())
    if front in d:
        if len(d[front]) == 1:
            print(d[front][0])
        else:
            print('?')
    else:
        print('!')