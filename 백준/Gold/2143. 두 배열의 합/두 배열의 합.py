from collections import Counter

def get_sub_sums(arr):
    sub_sums = []
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            sub_sums.append(s)
    return sub_sums

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

subA = get_sub_sums(A)
subB = get_sub_sums(B)
countB = Counter(subB)

ans = 0
for a in subA:
    ans += countB[T - a]

print(ans)
