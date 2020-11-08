import sys

line = sys.stdin.readline().strip().split(" ")
n = int(line[0])
h = int(line[1])
v = int(line[2])

q1 = h*v*4
q2 = (n-h)*v*4
q3 = h*(n-v)*4
q4 = (n-h)*(n-v)*4

quads = [q1,q2,q3,q4]
print(max(quads))
