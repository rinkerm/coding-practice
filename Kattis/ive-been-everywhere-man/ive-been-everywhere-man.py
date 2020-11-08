import sys

t = int(sys.stdin.readline())

for i in range(0,t):
	n = int(sys.stdin.readline())
	cities = {}
	running_sum = 0
	for j in range(0,n):
		city = sys.stdin.readline()
		if(not (city in cities)):
			cities[city] =1
			running_sum+=1
	print(running_sum)

