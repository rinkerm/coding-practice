import re

regex = r'\(([\+-]?(?:[1-9]\d|\d)(?:\.\d+)?, [\+-]?(?:1\d\d|[1-9]\d|\d)(?:\.\d+)?)\)'

n = int(input())

for i in range(0,n):
    s = input()
    matches = re.findall(regex,s)
    if len(matches) > 0:
        x,y = matches[0].split(', ')
        if x == '+0' or x == '-0' or y == '+0' or y == '-0':
            print('Invalid')
        else:
            
            x = float(x.replace('+',''))
            y = float(y.replace('+',''))
            if x>=-90.0 and x<=90.0 and y>= -180.0 and y<=180.0:
                print('Valid')
            else:
                print('Invalid')
    else:
        print('Invalid')
                
