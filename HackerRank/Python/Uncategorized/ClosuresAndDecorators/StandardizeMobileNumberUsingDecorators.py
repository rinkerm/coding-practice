import re
regex= r'\+?(?:91|0)?(\d{5})(\d{5})'
def wrapper(f):
    def fun(l):
        nums = []
        for s in l:
            m = re.findall(regex,str(s))
            nums.append('+91 ' + m[0][0] + ' ' + m[0][1])
        f(nums)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
