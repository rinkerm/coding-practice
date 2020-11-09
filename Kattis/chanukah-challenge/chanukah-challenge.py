import sys

n = int(sys.stdin.readline())

for i in range(0,n):
	line = sys.stdin.readline().strip().split(" ")
	candles = 0
	for j in range(0,int(line[1])):
		candles += (j+2)
	print(line[0],candles)
