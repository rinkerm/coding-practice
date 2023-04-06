import numpy
a = list(map(float,input().split()))
x = int(input())
print(numpy.polyval(a,x))
