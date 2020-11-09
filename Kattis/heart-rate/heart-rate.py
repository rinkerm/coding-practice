import sys

def beats(b,p):
	BPM = (60*b) / p
	minABPM = BPM - (60/p)
	maxABPM = BPM + (60/p)
	return(minABPM,BPM,maxABPM)

n = int(sys.stdin.readline())
for i in range(0,n):
	line = sys.stdin.readline().strip().split(" ")
	b = int(line[0])
	p = float(line[1])
	minABPM, BPM, maxABPM = beats(b,p)
	print(minABPM,BPM,maxABPM)
