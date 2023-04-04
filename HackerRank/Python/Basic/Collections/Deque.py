from collections import deque
n = int(input())
d = deque()
for i in range(0,n):
    args = input().split()
    if args[0] == 'append':
        d.append(int(args[1]))
    elif args[0] == 'appendleft':
        d.appendleft(int(args[1]))
    elif args[0] == 'pop':
        d.pop()
    elif args[0] == 'popleft':
        d.popleft() 
for v in d:
    print(v,end=' ')
