import re
regex = r'^([_|\.]\d+[a-zA-Z]*_?)$'
n = int(input())

for i in range (0,n):
    s = input()
    matches = re.findall(regex,s)
    if(len(matches))>0:
        print('VALID')
    else:
        print('INVALID')
