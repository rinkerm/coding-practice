import re
zero_to_255 = '(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])'
regex1 = '^{0}\.{0}\.{0}\.{0}$'.format(zero_to_255)
zero_to_ffff = '[0-9a-f]{1,4}'
regex2 = '^{0}:{0}:{0}:{0}:{0}:{0}:{0}:{0}$'.format(zero_to_ffff)
n = int(input())
for i in range (0,n):
    s = input()
    matches = re.findall(regex1,s)
    matches2 = re.findall(regex2,s)
    if(len(matches))>0 and len(matches[0])==4:
        print('IPv4')
    elif(len(matches2))>0:
        print('IPv6')
    else:
        print('Neither')
