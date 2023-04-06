n = int(input())
for i in range(0,n):
    d = dict()
    s = input()
    nums = 0
    upper = 0
    v = 0
    for c in s:
        if not c.isalnum():
            v = 1
            break
        if not c in d:
            d[c] = 1
        else:
            v = 1
            break
        nums+=int(c.isnumeric())
        upper+=int(c.isupper())
    if nums < 3 or upper < 2 or v != 0 or len(s) != 10:
        print('Invalid')
    else:
        print('Valid')
        
            
