#16165 걸그룹 마스터 준석이

group = {} 
idol = {} 

N, M = map(int, input().split())


for _ in range(N):
    groupName = input()
    group[groupName] = [] 
    for _ in range(int(input())):
        idolName = input()
        group[groupName].append(idolName)
        idol[idolName] = groupName
    group[groupName] = sorted(group[groupName]) 

for _ in range(M):
    keyword = input()

    if int(input()):
        print(idol[keyword])
    else:
        print('\n'.join(group[keyword]))