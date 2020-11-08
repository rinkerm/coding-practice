import sys

def count_points(n):
	if(n==1):
		return(3,9)
	else:
		oldside,oldpoints = count_points(n-1)
		side = (oldside *2)-1
		points = (oldpoints*4)-(side*2)-1
		return(side,points)	

n = int(sys.stdin.readline())
s,p = count_points(n)
print(p)

