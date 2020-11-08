import sys

line = sys.stdin.readline()
line = line.split(" ")
n = int(line[0])
P = int(line[1])

desc = []
for i in range(0,n):
	desc.append(sys.stdin.readline())
print(P)
