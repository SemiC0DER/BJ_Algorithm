#25192 

N = int(input())
hello = set()
gom = 0

for i in range(N):
    log = input()
    if log == 'ENTER':
        gom += len(hello)
        hello.clear()
    else:
        hello.add(log)

gom += len(hello)
print(gom)