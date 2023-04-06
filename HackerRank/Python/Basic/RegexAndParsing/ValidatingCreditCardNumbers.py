import re
r1 = r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
r2 = r'(\d)-?\1-?\1-?\1'
n = int(input())
for i in range(0,n):
    s = input()
    m = re.findall(r1,s)
    ans = 'Invalid'
    if len(m) > 0:
        s=s.replace('-','')
        m = re.findall(r2,s)
        if len(m) == 0:
            ans = 'Valid'
    print(ans)
