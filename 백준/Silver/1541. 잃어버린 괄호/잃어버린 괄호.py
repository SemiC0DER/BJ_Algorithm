def formula(string):
    ret = 0
    num = ''
    for i in range(len(string)):
        if string[i] == '+':
            ret += int(num)
            num = ''
        else:
            num += string[i]
    ret += int(num)
    return ret

a = input().split('-')
ans = formula(a[0])
for string in a[1:]:
    ans -= formula(string)
print(ans)