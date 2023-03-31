import re
regex = r'\b\W*?({})\W*?\b'
n = int(input())
s=''
for i in range(0,n):
    s+= input() + '\n'
t = int(input())
for i in range(0,t):
    word = input()
    pattern = regex.format(word)
    print(len(re.findall(pattern,s))) 
