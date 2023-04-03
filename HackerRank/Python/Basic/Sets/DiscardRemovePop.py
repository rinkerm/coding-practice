n = int(input())
s = set(map(int, input().split()))

N = int(input())
for i in range(0,N):
    line = input().split(' ')
    command = line[0]
    if command == 'pop':
        s.pop()
    elif command == 'remove':
        s.remove(int(line[1]))
    elif command == 'discard':
        s.discard(int(line[1]))
print(sum(s))
