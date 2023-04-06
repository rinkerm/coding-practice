import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    n = numpy.array(arr,float)
    return n[::-1]
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
