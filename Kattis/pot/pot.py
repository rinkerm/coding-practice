import sys

n = int(sys.stdin.readline())
running_sum = 0
for i in range(0,n):
	line = sys.stdin.readline().strip()
	x = int(line[0:len(line)-1])
	p = int(line[len(line)-1:])
	running_sum+= x**p
print(running_sum)
