a = int(input())
A = set(map(int,input().split(' ')))

N = int(input())
for i in range(0,N):
    command = input().split(' ')
    B = set(map(int,input().split(' ')))
    if command[0] == 'intersection_update':
        A.intersection_update(B)
    elif command[0] == 'update':
        A.update(B)
    elif command[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif command[0] == 'difference_update':
        A.difference_update(B)
print(sum(A))
    
