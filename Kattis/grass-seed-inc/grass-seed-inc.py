import sys

cost = float(sys.stdin.readline())
n = int(sys.stdin.readline())

totalcost = 0
for i in range(0,n):
	line = sys.stdin.readline().strip().split(" ")
	totalcost += ((float(line[0]) * float(line[1])) * cost)


print(totalcost)
