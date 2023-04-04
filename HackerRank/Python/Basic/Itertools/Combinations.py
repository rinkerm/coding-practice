from itertools import combinations
args = input().split(' ')
s = args[0]
k = int(args[1])
for i in range(1,k+1):
    perms = list(combinations(s,i))
    for j in range(0,len(perms)):
        perms[j] = list(perms[j])
        perms[j].sort()
    perms.sort()
    for perm in perms:
        print(''.join(map(str, perm)))
