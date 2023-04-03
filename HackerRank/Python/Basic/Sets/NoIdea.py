score = 0
#we can ignore n,m
line = input()
#read in array
arr = []
nums = {}
line = input()
for v in line.split(' '):
    v = int(v)
    if v in nums:
        nums[v]+=1
    else:
        nums[v]=1
    arr.append(int(v))
ARR = set(arr)
#read in A
A = []
line = input()
for v in line.split(' '):
    A.append(int(v))
a =set(A)
#read in B
B = []
line = input()
for v in line.split(' '):
    B.append(int(v))
b =set(B)
#calculate score
for v in ARR.intersection(A):
    if v in nums:
        score += nums[v]
for v in ARR.intersection(B):
    if v in nums:
        score -= nums[v]
print(score)

