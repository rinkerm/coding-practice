# Enter your code here. Read input from STDIN. Print output to STDOUT
line = input()
args = line.split(' ')

N = int(args[0])
M = int(args[1])

n = N//2
s =''
sub='.|.'

for i in range(0,n):
    mid = sub*((2*i)+1)
    left = '-'*((M-len(mid))//2)
    right = '-'*((M-len(mid))//2)
    s+=left+mid+right+'\n'
s+=('-'*((M-7)//2))+'WELCOME'+('-'*((M-7)//2))+'\n'
for i in range(n-1,-1,-1):
    mid = sub*((2*i)+1)
    left = '-'*((M-len(mid))//2)
    right = '-'*((M-len(mid))//2)
    s+=left+mid+right+'\n'  
print(s)
