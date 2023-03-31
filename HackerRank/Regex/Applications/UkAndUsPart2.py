import re

regex = r'\b({}(?:{}{}|{}){})\b'

n = int(input())

s = ''

for i in range(0,n):
    s += input() + '\n'

t = int(input())
for j in range(0,t):
    w = input()
    x = w.find('our')
    w1 = w[:x]
    w2 = w[x:x+1]
    w3 = w[x+1:x+2]
    w4 = w[x+2:]
    matches = re.findall(regex.format(w1,w2,w3,w2,w4),s)
    print(len(matches))
