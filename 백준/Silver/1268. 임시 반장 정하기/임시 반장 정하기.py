N = int(input())
cls = [[set([]) for _ in range(10)] for _ in range(5)]
student_class = []

for i in range(1, N + 1):
    j = 0
    tmp = list(map(int, input().split()))
    student_class.append(tmp)
    for my_cls in tmp:
        cls[j][my_cls].add(i)
        j += 1

friends = 0
leader = 1
my_friend = 0
for i in range(1, N + 1):
    my_friend = set()
    for j in range(5):
        my_cls = student_class[i - 1][j]
        my_friend = set.union(my_friend, cls[j][my_cls])
    my_friend.discard(i)
    if len(my_friend) > friends:
        friends = len(my_friend)
        leader = i
        
print(leader)
