import sys

n = int(sys.stdin.readline())

running_sum = 0.000

for i in range(0,n):
	line = sys.stdin.readline().split(" ")
	q = float(line[0])
	y = float(line[1])
	running_sum += (q*y)
print(running_sum)
