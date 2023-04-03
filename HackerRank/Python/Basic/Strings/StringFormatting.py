def print_formatted(number):
    s =''
    spacer = len(format(number,'b'))
    for i in range(1,number+1):
        octal = format(i,'o')
        hexs = format(i,'x')
        binary = format(i,'b')
        s+=str(i).rjust(spacer)+' '+octal.rjust(spacer)+' ' +hexs.upper().rjust(spacer)+' '+binary.rjust(spacer)+'\n'
    s=s[:len(s)-1]
    print(s)    
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
