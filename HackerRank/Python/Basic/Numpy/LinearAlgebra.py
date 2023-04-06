import numpy
n = int(input())
a = []
for i in range(0,n):
    r = list(map(float,input().split()))
    a.append(r)
a = numpy.array(a)
print(numpy.linalg.det(a).round(decimals=2))
