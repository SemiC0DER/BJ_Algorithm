#9536 여우는 어떻게 울지

T = int(input())
for _ in range(T):
    raw = input().rstrip().split()
    wild = set(raw)
    while True:
        animal = input().rstrip().split()
        if len(animal) == 5:
            break
        wild.discard(animal[2])

    for i in range(len(raw)):
        if raw[i] in wild:
            print(raw[i], end = ' ')