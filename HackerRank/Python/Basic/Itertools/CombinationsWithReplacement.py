from itertools import combinations_with_replacement
args = input().split(' ')
s = args[0]
k = int(args[1])
perms = list(combinations_with_replacement(s,k))
for j in range(0,len(perms)):
    perms[j] = list(perms[j])
    perms[j].sort()
perms.sort()
for perm in perms:
    print(''.join(map(str, perm)))
