import sys

'''
line = sys.stdin.readline().strip()
line += "!"
line = line.split("<")
text = ''
for part in line:
	if(len(part)>0):
		text = text + part[0:len(part)-1]
	else:
		text = text[0:len(text)-1]
print(text)
'''
x = "abc"
print(x)
x.remove(2)
print(x)
