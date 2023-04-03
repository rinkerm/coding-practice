if __name__ == '__main__':
    N = int(input())
    listed = []
    for i in range(0,N):
        commands = input().split(' ')
        if commands[0] == 'insert':
            listed.insert(int(commands[1]),int(commands[2]))
        elif commands[0] == 'print':
            print(listed)
        elif commands[0] == 'remove':
            listed.remove(int(commands[1]))
        elif commands[0] == 'append':
            listed.append(int(commands[1]))
        elif commands[0] == 'sort':
            listed.sort()
        elif commands[0] == 'pop':
            listed.pop()
        elif commands[0] == 'reverse':
            listed.reverse()
