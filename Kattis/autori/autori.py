import sys

names = sys.stdin.readline().strip().split("-")
abbv = ''
for name in names:
	abbv+=name[0]
print(abbv)
