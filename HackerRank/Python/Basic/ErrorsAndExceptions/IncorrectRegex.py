import re
n = int(input())
for i in range(0,n):
    regex = input()
    try:
        re.findall(regex,'')
        print(True)
    except Exception as e:
        print('False')
