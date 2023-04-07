from collections import OrderedDict
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        d = OrderedDict()
        s = string[i:i+k]
        for c in s:
            if not c in d:
                d[c] = 1
        for key in d.keys():
            print(key,end='')
        print()
            
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
