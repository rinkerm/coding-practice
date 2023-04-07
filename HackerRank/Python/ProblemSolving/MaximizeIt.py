from itertools import product
l = list(map(int,input().split()))
K = l[0]
M = l[1]
a = []
for i in range(0,K):
    l = list(map(int,input().split()))
    b = []
    for j in range(1,l[0]+1):
        b.append(l[j]**2)
    a.append(b)
c = [p for p in product(*a)]
m = 0
for choice in c:
    s = sum(choice)%M
    if m<s:
        m=s
print(m)

