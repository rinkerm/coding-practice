import numpy
args = list(map(int,input().split()))
a = []
for i in range(0,args[0]):
    r = list(map(int,input().split()))
    a.append(r)
a = numpy.array(a)
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(numpy.std(a,axis=None).round(decimals=11))
