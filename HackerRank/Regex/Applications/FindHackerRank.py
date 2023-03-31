import re

start = r'^(hackerrank)'
end = r'(hackerrank)$'

n = int(input())

for i in range(0,n):
    s = input()
    starts = re.findall(start,s)
    ends = re.findall(end,s)
    
    if len(starts)> 0 and len(ends)>0:
        print(0)
    elif len(starts) > 0:
        print(1)
    elif len(ends) > 0:
        print(2)
    else:
        print(-1)
