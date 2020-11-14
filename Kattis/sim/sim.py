import sys
n = int(sys.stdin.readline())
for i in range(0,n):
	line = sys.stdin.readline().strip()
	text = ''
	index = 0
	for char in line:
		if(char == '<'):
			if(not index==0):
				text = text[:index-1] + text[index:]
				index-=1
		elif(char == '['):
			index = 0
		elif(char == ']'):
			index = len(text)
		else:
			text = text[:index] + char + text[index:]
			index+=1
	print(text)
				
