import numpy
args = list(map(int,input().split()))
a = []
for i in range(0,args[0]):
    r = list(map(int, input().split()))
    a.append(r)
a = numpy.array(a)
print(numpy.transpose(a))
print(a.flatten())


