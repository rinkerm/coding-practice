import re
regex = r'<a href="([\S ]*?)".*?>([\w ,\.\/]*?)(?=<\/)'

n = int(input())
for i in range (0,n):
    s = input()
    matches = re.findall(regex,s)
    for match in matches:
        print(match[0]+','+match[1].strip())

