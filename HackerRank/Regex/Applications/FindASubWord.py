import re
regex = r'\b[\w_]+({})[\w_]+\b'
n = int(input())
s = ''
for i in range (0,n):
    s += input() + '\n'
m = int(input())
for j in range(0,m):
    q = input()
    matches = re.findall(regex.format(q),s)
    print(len(matches))
