import re
regex = r'^[789]\d{9}$'
n = int(input())
for i in range(0,n):
    s = input()
    m = re.findall(regex,s)
    if len(m) > 0:
        print('YES')
    else:
        print('NO')

