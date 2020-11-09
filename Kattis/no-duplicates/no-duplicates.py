import sys

def duplicates(words):
	dictionary = {}
	for word in words:
		if(word in dictionary):
			return("no")
		else:
			dictionary[word] = 1
	return("yes")

line = sys.stdin.readline().strip().split(" ")
print(duplicates(line))

