M = int(input())
line = input()
m = set()
for v in line.split(' '):
    m.add(int(v))
N = int(input())
line = input()
n = set()
for v in line.split(' '):
    n.add(int(v))
mn = m.symmetric_difference(n)

ans = []
for v in mn:
    ans.append(v)
ans.sort()
for v in ans:
    print(v)

