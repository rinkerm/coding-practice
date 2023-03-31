import re

regex = '(hackerrank)'

n = int(input())

hackerranks = 0
for i in range(0,n):
    s = input().lower()
    matches = re.findall(regex,s)
    if(len(matches)>0):
        hackerranks+=1
print(hackerranks)
