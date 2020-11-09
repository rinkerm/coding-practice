import sys

def hiss_check(word):
	previous = ''
	for char in word:
		if(previous == 's' and char == 's'):
			return("hiss")
		else:
			previous = char
	return "no hiss"

word = sys.stdin.readline().strip()
print(hiss_check(word))

