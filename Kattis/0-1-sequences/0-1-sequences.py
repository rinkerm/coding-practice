import sys

FIXED_MOD = 1000000007
twok = {0:1,1:2}
def two_powK(k):
	if(k in twok):
		return twok[k]
	else:
		twok[k] = (2*twok[k-1]) % FIXED_MOD
		return twok[k] 

raw_sequence = sys.stdin.readline().strip()

k = 0 # number of question marks
o = 0 # number of zeroes
inversions = 0

for char in raw_sequence[::-1]:
	if(char == "1"):
		oInversions = o*two_powK(k)
		if(k==0):
			kInversions = 0
		else:
			kInversions = k*two_powK(k-1)
		inversions = (inversions + oInversions + kInversions) % FIXED_MOD
	elif(char == "?"):
		inversions *= 2
		oInversions = o*two_powK(k)
		if(k==0):
			kInversions = 0
		else:
			kInversions = k*two_powK(k-1)
		inversions = (inversions + oInversions + kInversions) % FIXED_MOD
		k+=1
	else:
		o +=1

print(inversions)

