from collections import OrderedDict
d = OrderedDict()
n = int(input())
for i in range(0,n):
    args = input().rsplit(' ',1)
    if(args[0] in d):
        d[args[0]]+=int(args[1])
    else:
        d[args[0]]=int(args[1])
for key in d:
    print(key,d[key])
    
