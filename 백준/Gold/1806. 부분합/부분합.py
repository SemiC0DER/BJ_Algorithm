N, S = map(int, input().split())
num = [0] + list(map(int, input().split())) + [0]

def sol():
    ans = N
    left, right = 0, 1
    part = num[1]
    while right <= N:
        if left > right:
            break

        if part >= S:
            ans = min(ans, right - left)
            left += 1
            part -= num[left]
        else:
            right += 1
            part += num[right]
    return ans

if sum(num) < S:
    print(0)
else:
    print(sol())