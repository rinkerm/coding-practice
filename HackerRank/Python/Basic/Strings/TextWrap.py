import textwrap

def wrap(string, max_width):
    s = ''
    for i in range(0,len(string)):
        if (i+1)%max_width==0:
            s+=string[i:i+1]+'\n'
        else:
            s+=string[i:i+1]
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
