import numpy
a = []
args = list(map(int,input().split()))
for i in range(0,args[0]):
    x = list(map(int,input().split()))
    a.append(x)
a = numpy.array(a)
b = []
for i in range(0,args[1]):
    y = list(map(int,input().split()))
    b.append(y)
b = numpy.array(b)

print(numpy.concatenate((a,b),axis=0))
