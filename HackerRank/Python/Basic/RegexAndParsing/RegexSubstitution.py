import re
r1 = r'(?<=\s)(\&\&)(?=\s)' 
r2 = r'(?<=\s)(\|\|)(?=\s)' 
n = int(input())
for i in range(0,n):
    s = input()
    print(re.sub(r2,'or', re.sub(r1,'and', s)))

