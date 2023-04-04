from collections import OrderedDict
d = OrderedDict()
n = int(input())
for i in range(0,n):
    w = input()
    if w in d:
        d[w]+=1
    else:
        d[w]=1
print(len(d))
for key in d:
    print(d[key],end=' ')
