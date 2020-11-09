import sys

n = int(sys.stdin.readline())
line = sys.stdin.readline().strip().split(" ")

below_zeroes = 0
for i in range(0,n):
	if(int(line[i])<0):
		below_zeroes+=1
print(below_zeroes)
