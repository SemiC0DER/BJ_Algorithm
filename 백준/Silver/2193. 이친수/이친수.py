pinary = [1] * 2
N = int(input())
for i in range(N - 1):
    pinary[0], pinary[1] = pinary[0] + pinary[1], pinary[0]
print(pinary[1])