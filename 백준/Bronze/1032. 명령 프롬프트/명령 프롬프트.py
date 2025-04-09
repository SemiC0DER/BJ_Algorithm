#1032 명령 프롬프트

N = int(input())
prompt = list(input())

for i in range(N - 1):
    file_name = list(input())
    for j in range(len(prompt)):
        if prompt[j] != file_name[j]:
            prompt[j] = '?'

print(''.join(prompt))