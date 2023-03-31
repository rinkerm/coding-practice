import re
regex = r'([A-Za-z\d_]+?(?:\.[A-Za-z\d_]+)*@[A-Za-z\d_]+(?:\.[A-Za-z\d_]+)*)'

n = int(input())
s = ''
for i in range(0,n):
    s+= input() + '\n'

matches = re.findall(regex,s)

result = ''
matches.sort()
uniques = []
for match in matches:
    if match not in uniques:
        uniques.append(match)

if len(uniques)>0:
    result = uniques[0]
    for j in range(1,len(uniques)):
        result += ';' + uniques[j]
print(result)
