n = int(input())
A = list(map(int,input().split(' ')))
a = set(A)
print(((sum(a)*n)-sum(A))//(n-1))

