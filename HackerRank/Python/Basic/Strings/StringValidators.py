def alphanumeric(s):
    for char in s:
        if str(char).isalnum():
            return True
    return False
    
def alphabetical(s):
    for char in s:
        if str(char).isalpha():
            return True
    return False
            
def digit(s):
    for char in s:
        if str(char).isdigit():
            return True
    return False

def lower(s):
    for char in s:
        if str(char).islower():
            return True
    return False
    
def upper(s):
    for char in s:
        if str(char).isupper():
            return True
    return False
    
if __name__ == '__main__':
    s = input()
    print(alphanumeric(s))
    print(alphabetical(s))
    print(digit(s))
    print(lower(s))
    print(upper(s))
