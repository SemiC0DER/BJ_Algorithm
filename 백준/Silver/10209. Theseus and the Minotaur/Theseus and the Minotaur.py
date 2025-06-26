N = int(input())
op = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}

for i in range(N):
    s = input().strip()
    stack = []
    for ch in s:
        if stack and stack[-1] == op[ch]:
            stack.pop()
        else:
            stack.append(ch)
    
    print(f'Data Set {i + 1}:')
    print('Yes' if not stack else 'No')
    print()
