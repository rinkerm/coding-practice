import re

regex = r'^(\d{1,3})[ -]?(\d{1,3})[ -]?(\d+)$'

n = int(input())

for i in range(0,n):
    s = input()
    matches = re.findall(regex,s)
    
    out = 'CountryCode={},LocalAreaCode={},Number={}'.format(matches[0][0],matches[0][1],matches[0][2])
    print(out)
