import re
regex = r'<(\w+?)[ >]'
n = int(input())
tags = []
for i in range (0,n):
    s = input()
    matches = re.findall(regex,s)
    if len(matches)>0:
        for tag in matches:
            if tag not in tags:
                tags.append(tag)
tags.sort()
out = ''
for tag in tags:
    out+=tag+';'
out = out[:len(out)-1]
print(out)
