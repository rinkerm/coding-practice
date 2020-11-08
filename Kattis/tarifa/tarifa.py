import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

running_sum = x
for i in range(0,n):
	P_i = int(sys.stdin.readline())
	running_sum +=x
	running_sum -=P_i
print(running_sum)


