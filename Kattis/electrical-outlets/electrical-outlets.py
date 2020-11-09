import sys

def usable_outlets(strips):
	outlets = 1 - len(strips)
	for strip in strips:
		outlets += strip
	return outlets

n = int(sys.stdin.readline())

for i in range(0,n):
	line = sys.stdin.readline().strip().split(" ")
	count = int(line[0])
	strips = []
	for j in range(1,count+1):
		strips.append(int(line[j]))
	print(usable_outlets(strips))
