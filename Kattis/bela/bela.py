import sys

dominant = {"A":11,"K":4,"Q":3,"J":20,"T":10,"9":14,"8":0,"7":0}
not_dominant = {"A":11,"K":4,"Q":3,"J":2,"T":10,"9":0,"8":0,"7":0}

first = sys.stdin.readline().strip().split(" ")
point_lookup = {}
suits = ["H","C","S","D"]
n = int(first[0])
for suit in suits:
	if(suit == first[1]):
		point_lookup[suit] = dominant
	else:
		point_lookup[suit] = not_dominant
points = 0
for i in range(0,(4*n)):
	card = sys.stdin.readline()
	points+=point_lookup[card[1:2]][card[0:1]]
print(points)
