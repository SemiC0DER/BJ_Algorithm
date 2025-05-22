N = int(input())
mooray = [3]
moo = ['m', 'o', 'o']
while mooray[-1] < N:
    k = len(mooray)
    mooray.append(mooray[-1] + 1 + k + 2 + mooray[-1])

idx = len(mooray) - 1
loc = N
ans = None
while idx > 0:
    if loc <= mooray[idx - 1]:
        idx -= 1
    elif loc <= mooray[idx - 1] + idx + 2:
        if loc == mooray[idx - 1] + 1:
            ans = 'm'
        else:
            ans = 'o'
        break
    else:
        loc -= mooray[idx - 1] + idx + 3
        idx -= 1

print(ans if ans is not None else moo[loc - 1])