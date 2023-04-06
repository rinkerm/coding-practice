import re
regex = r'(?<!^)(#[\dA-Fa-f]{3}(?:[\dA-Fa-f]{3})?)'
n = int(input())
for i in range(0,n):
    s = input()
    m = re.findall(regex,s)
    for match in m:
        print(match)
