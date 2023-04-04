from collections import deque
t = int(input())
for i in range(0,t):
    ans = 'Yes'
    b = int(input())
    blocks = deque(list(map(int,input().split())))
    size = 0
    for i in range(0,b):
        if blocks[0]>=blocks[len(blocks)-1]:
            next_block = blocks[0]
            if size>=next_block or size == 0:
                blocks.popleft()
                size = next_block
            else:
                ans = 'No'
                break
        else:
            next_block = blocks[len(blocks)-1]
            if size>=next_block or size == 0:
                blocks.pop()
                size = next_block
            else:
                ans = 'No'
                break
    print(ans)
    
