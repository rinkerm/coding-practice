import sys

inputs = sys.stdin.readline().strip().split(" ")
e = int(inputs[0])
f = int(inputs[1])
c = int(inputs[2])

bottles = e + f
consumed = 0
while(True):
	if(int(bottles/c)==0):
		break
	else:
		newbottles = int(bottles/c)
		keptbottles = bottles%c
		consumed+=newbottles
		bottles = newbottles+keptbottles
print(consumed)

