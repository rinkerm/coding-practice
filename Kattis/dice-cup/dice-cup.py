import sys

dice = sys.stdin.readline().strip().split(" ")
die1 = int(dice[0])
die2 = int(dice[1])
outcomes = {}
for i in range(1,die1+1):
	for j in range(1,die2+1):
		outcome = i + j
		if(outcome not in outcomes):
			outcomes[outcome] = 1
		else:
			outcomes[outcome] += 1
probabilities = {}
for key in outcomes:
	if(outcomes[key] in probabilities):
		probabilities[outcomes[key]].append(key)
	else:
		probabilities[outcomes[key]] = [key]
		
highest_prob = probabilities[max(probabilities.keys())]

for ans in highest_prob:
	print(ans)
