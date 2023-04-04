import itertools
n = int(input())
letters = input().split(' ')
k = int(input())
combs = list(itertools.combinations(letters,k))
count = 0
for comb in combs:
    if 'a' in comb:
        count+=1
print(count/len(combs))
