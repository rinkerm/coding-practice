from itertools import product
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))
AxB = list(product(A,B))
for tup in AxB:
    print(tup,end=' ')

