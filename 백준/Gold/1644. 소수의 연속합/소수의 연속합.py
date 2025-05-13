#1644 소수의 연속합

def eratostenes(n):
    prime = [2]
    num = [True] * (n + 1)
    num[0], num[1] = False, False

    for i in range(4, n + 1, 2):
        num[i] = False

    for i in range(3, n + 1, 2):
        if num[i]:
            prime.append(i)
            for j in range(i + i, n + 1, i):
                num[j] = False

    return prime

def cont_sum(n):
    prime = eratostenes(n)
    buffer = prime[0]
    left, right = 0, 0
    count = 0
    while left <= right:
        if buffer > n:
            buffer -= prime[left]
            left += 1
        else:
            if buffer == n:
                count += 1
            right += 1
            if right == len(prime):
                break
            buffer += prime[right]
    
    return count

n = int(input())
print(cont_sum(n))