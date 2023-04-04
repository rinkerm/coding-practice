n = int(input())
for i in range(0,n):
    args = input().split()
    try:
        args = list(map(int,args))
        ans = args[0]/args[1]
        print(int(ans))
    except ZeroDivisionError as e:
        print("Error Code:", 'integer division or modulo by zero')
    except ValueError as e:
        print("Error Code:",e)

