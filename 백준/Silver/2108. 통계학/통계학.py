#2108 통계학

import sys
input = sys.stdin.readline

N = int(input())
nums = [0] * 8001

for i in range(N):
    nums[int(input()) + 4000] += 1

count = 0
mode = [0, 0, 0] #counted, number, 2nd?
middle = None
small = None
big = None
av = 0

for i in range(8001):
    if nums[i] == 0:
        continue

    number = i - 4000
    av += number * nums[i]
    count += nums[i]

    if nums[i] > mode[0]:
        mode = [nums[i], number, 1]
    elif nums[i] == mode[0]:
        if mode[2] == 1:
            mode = [nums[i], number, 2]

    if middle is None and count > N // 2:
        middle = number

    if small is None:
        small = number

    big = number

print(round(av / N), middle, mode[1], big - small, sep = '\n')