import sys

line = sys.stdin.readline()
line = line.split(" ")

r1 = int(line[0])
s = int(line[1])

r2 = (s*2)-r1

print(r2)
