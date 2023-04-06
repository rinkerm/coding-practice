import re
regex = r'^[\-+]?\d*\.\d+$'
n = int(input())
for i in range(0,n):
    s = input()
    print(len(re.findall(regex,s))>0)
