import re

regex = r'[A-Z]{5}\d{4}[A-Z]'

n = int(input())

for i in range(0,n):
    s = input()
    if len(re.findall(regex,s)) > 0:
        print('YES')
    else:
        print('NO')
