import sys

def costs(r,e,c):
	if(r>e-c):
		return("do not advertise")
	elif(e-c>r):
		return("advertise")
	else:
		return("does not matter")

n = int(sys.stdin.readline())

for i in range(0,n):
	line = sys.stdin.readline().strip().split(" ")
	print(costs(int(line[0]),int(line[1]),int(line[2])))

