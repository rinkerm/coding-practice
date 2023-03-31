import re

regex = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'

n = int(input())

for i in range(0,n):
    s = input()
    if len(re.findall(regex,s)) > 0:
        print('VALID')
    else:
        print('INVALID')
    
