import re
s = input()
r = input()
matches = 0
for i in range(0,len(s)-len(r)+1):
    if not re.match(r,s[i:i+len(r)]) is None:
        matches+=1
        print('({}, {})'.format(i,i+len(r)-1))
if matches == 0:
    print('({}, {})'.format(-1,-1))
