n, p = map(int, input().split())
w, l, g = map(int, input().split())
winner = set()

for _ in range(p):
    name, info = input().split()
    if info == 'W':
        winner.add(name)

score = 0
escape = False
for _ in range(n):
    if input() in winner:
        score += w
    else:
        if score - l < 0:
            score = 0
        else:
            score -= l
    if score >= g:
        print("I AM NOT IRONMAN!!")
        escape = True
        break

if not escape:
    print("I AM IRONMAN!!")