import sys
setno = 1
while(True):
	n = int(sys.stdin.readline())
	
	if(n==0):
		break
	else:
		print("SET {}".format(setno))
		setno+=1
		names = ['']*n
		pair = 0
		index1 = 0
		index2 = n-1
		for i in range(0,n):
			name = sys.stdin.readline().strip()
			if(pair):
				names[index2] = name
				index2-=1
				pair = 0
			else:
				names[index1] = name
				index1+=1
				pair = 1
		for name in names:
			print(name)
		
