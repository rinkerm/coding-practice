import numpy
args = list(map(int,input().split()))
a = []
for i in range(0,args[0]):
    r = list(map(int,input().split()))
    a.append(r)
a = numpy.array(a)
b = numpy.min(a, axis=1)
print(numpy.max(b))
