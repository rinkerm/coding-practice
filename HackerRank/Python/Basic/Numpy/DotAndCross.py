import numpy
n = int(input())
a = []
for i in range(0,n):
    r = list(map(int,input().split()))
    a.append(r)
a = numpy.array(a)
b=[]
for i in range(0,n):
    r = list(map(int,input().split()))
    b.append(r)
b = numpy.array(b)
print(numpy.dot(a,b))
