import numpy
numpy.set_printoptions(legacy='1.13')
args = list(map(int,input().split()))
print(numpy.eye(*args))
