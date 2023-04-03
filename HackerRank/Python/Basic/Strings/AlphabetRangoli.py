def print_rangoli(size):
    chr_base = 96
    len_r = (2*size)+(2*(size-1))-1
    s = []
    #top half
    for i in range(1,size):
        r = ''
        for j in range(0,i):
            r+=chr(chr_base+(size-j))+ '-'
        r=r[:len(r)-1]
        if(i>1):
            r=r+r[len(r)-2::-1]
        r=r.center(len_r,'-')
        s.append(r)
    #mid
    mid = ''
    for i in range(size,0,-1):
        mid+=chr(chr_base+i)+'-'
    mid = mid[:len(mid)-1]
    if(size > 1):
        mid = mid + mid[len(mid)-2::-1]
    s.append(mid)
    
    #bottom half
    for k in range(len(s)-2,-1,-1):
        s.append(s[k])
    for line in s:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
