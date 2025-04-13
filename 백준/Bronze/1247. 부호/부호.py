import sys
input = sys.stdin.readline

for _ in range(3):
    a = 0
    for _ in range(int(input())):
        a += int(input())
        
    if a > 0:
        print('+')
    elif a < 0:
        print('-')
    else:
        print('0')