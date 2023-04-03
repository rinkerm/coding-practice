vowels = ['A','E','I','O','U']

def minion_game(string):
    string = string.upper()
    s = 0
    k = 0
    for i in range(0,len(string)):
        sub = string[i]
        if sub[0:1] in vowels:
            k+=len(string)-i
        else:
            s+=len(string)-i
    if s>k:
        print('Stuart',s)
    elif k>s:
        print('Kevin',k)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
