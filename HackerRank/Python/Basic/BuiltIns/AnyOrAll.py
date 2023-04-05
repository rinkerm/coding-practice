n = int(input())
ints = input().split()
print(all([(int(x))>0 for x in ints]) and any([x==x[::-1] for x in ints]))
