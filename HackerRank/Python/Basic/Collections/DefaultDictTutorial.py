from collections import defaultdict
d = defaultdict(list)

args = input().split(' ')
n = int(args[0])
m = int(args[1])
for i in range(1,n+1):
    w = input()
    d[w].append(i)
for j in range(0,m):
    w = input()
    positions = d[w]
    if len(d[w])==0:
        print(-1)
    else:
        for pos in positions:
            print(pos,end=" ")
        print('')

