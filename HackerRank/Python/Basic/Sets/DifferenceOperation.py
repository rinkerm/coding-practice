n = int(input())
line = input().split()
A = set(line)
m = int(input())
line = input().split()
B = set(line)
print(len(A.difference(B)))