import sys
input = sys.stdin.readline
S,E,Q = input().split()

S = int(S[:2])*60 + int(S[3:])
E = int(E[:2])*60 + int(E[3:])
Q = int(Q[:2])*60+ int(Q[3:])

res = set()
result = 0
while True:
    try:
        time, name = input().split()
        time = int(time[:2])*60 + int(time[3:])

        if time <= S:
            res.add(name)
        elif name in res and (E<=time<=Q):
            res.remove(name)
            result +=1
    except:
        break


print(result)