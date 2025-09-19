s = input()
for i in range((len(s) - 1)//10 + 1):
    print(s[i*10:i*10+10])