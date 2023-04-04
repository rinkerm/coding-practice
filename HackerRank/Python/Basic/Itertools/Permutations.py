from itertools import permutations
args = input().split(' ')
s = args[0]
k = int(args[1])
perms = list(permutations(s,k))
perms.sort()
for perm in perms:
    print(''.join(map(str, perm)))
