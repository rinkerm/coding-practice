import re
regex = r'([a-zA-Z\d])\1'
s = input()
pos = -1
for i in range(0,len(s)-2):
    m = re.match(regex,s[i:i+2])
    if not m is None:
        pos = m.group(1)
        break
print(pos)
