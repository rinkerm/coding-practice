import sys
A = set(map(int,input().split(' ')))
t = int(input())

ans = False
i = 0
for i in range(0,t):
    B = set(map(int,input().split(' ')))
    
    superset = (A.issuperset(B) and len(A)>len(B))
    if i != 0 and superset != ans:
        ans = False
        break
    else:
        ans = superset
print(ans)
