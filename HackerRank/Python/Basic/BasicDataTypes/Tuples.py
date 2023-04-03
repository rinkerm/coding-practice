# Note this is written in python3 but due to issues with hacker rank's grading only a pypy3 solution is accepted
n = input()
line = input()
line = line.split(' ')
intLine = [int(v) for v in line]
t = tuple(intLine)
print(hash(t))

