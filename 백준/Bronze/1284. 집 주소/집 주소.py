while (s := input()) != '0':
    one = s.count('1')
    zero = s.count('0')
    l = zero - one + 4 * len(s) + 1
    print(l)