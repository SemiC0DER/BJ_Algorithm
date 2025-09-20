for i in range(int(input())):
    s = input()
    a = ['a', 'e', 'i', 'o', 'u']
    n = 0
    for i in s:
        if i in a:
            n += 1
    print(f"The number of vowels in {s} is {n}.")