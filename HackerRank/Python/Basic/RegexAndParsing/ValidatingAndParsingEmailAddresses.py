import email.utils
import re
regex = r'^[A-Za-z][A-Za-z\d\-\._]*@[A-Za-z]+\.[A-Za-z]{1,3}$'
n = int(input())
for i in range(0,n):
    s = input()
    p = email.utils.parseaddr(s)
    m = re.findall(regex,p[1])
    if len(m)>0:
        print(s)
    
