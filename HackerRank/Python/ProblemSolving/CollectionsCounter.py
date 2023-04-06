from collections import Counter
x = int(input())
shoes = list(map(int,input().split()))
stock = Counter(shoes)
n = int(input())
sum = 0
for i in range(0,n):
    cust = list(map(int,input().split()))
    if cust[0] in stock and stock[cust[0]] > 0:
        sum += cust[1]
        stock[cust[0]]-=1
print(sum)
