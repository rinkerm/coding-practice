import re

regex = r'\b({}(?:ze|se))\b'

n = int(input())

s = ''
for i in range(0,n):
    s += input() + '\n'

t = int(input())
for j in range(0,t):
    w = input()
    w = w[:len(w)-2]
    matches = re.findall(regex.format(w),s)
    print(len(matches))
    
    
