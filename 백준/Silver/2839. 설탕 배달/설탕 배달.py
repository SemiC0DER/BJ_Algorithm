#2839 설탕배달

N = int(input())
bag = 0

while N > 0:
    if N % 5 == 0:
        bag += N // 5
        N = 0
        break
    N -= 3
    bag += 1

if N != 0:
    print(-1)
else:
    print(bag)