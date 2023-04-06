import re
regex = r'[^aeiouAEIOU+\-\d\s]?([aeiouAEIOU]{2,})[^aeiouAEIOU+\-\d\s]'
s = input()
m = re.findall(regex,s)
if len(m) == 0:
    print(-1)
else:
    for match in m:
        print(match)
