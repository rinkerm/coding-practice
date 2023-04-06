import numpy
args = list(map(int,input().split()))
a = []
b = []
for i in range(0,args[0]):
    r = list(map(int,input().split()))
    a.append(r)
a = numpy.array(a,int)
for i in range(0,args[0]):
    r = list(map(int,input().split()))
    b.append(r)
b = numpy.array(b,int)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
