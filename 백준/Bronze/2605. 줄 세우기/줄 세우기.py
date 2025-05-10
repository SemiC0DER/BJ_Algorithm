student_number = int(input())
array = [int(x) for x in input().split()]

answer = [] 
for i in range(student_number):
    if array[i] == 0:
        answer.append(i+1)
    elif array[i] != 0:
        answer.insert(len(answer)-array[i],i+1)
print(*answer)