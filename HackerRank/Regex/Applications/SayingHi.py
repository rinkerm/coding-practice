import re

regex = r'^[Hh][Ii]\s[^Dd]'

n = int(input())

for i in range(0,n):
    s = input()
    
    if len(re.findall(regex,s)) > 0:
        print(s)
