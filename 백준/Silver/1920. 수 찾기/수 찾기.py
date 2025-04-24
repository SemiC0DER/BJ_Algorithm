N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
array = list(map(int, input().split()))

for i in range(M):
    start, end = 0, N - 1
    while(start <= end):
        n = (start + end) // 2
        
        if (A[n] == array[i]):
            print(1)
            break
        elif (A[n] > array[i]):
            end = n - 1
        else:
            start = n + 1

        if (start > end):
            print(0)
            break

