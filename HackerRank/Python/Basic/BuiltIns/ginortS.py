s = list(input())
odd = []
even = []
upper = []
lower = []
for char in s:
    if char.isdigit():
        if int(char)%2 == 1:
            odd.append(char)
        else:
            even.append(char)
    elif char.isupper():
        upper.append(char)
    else:
        lower.append(char)
odd.sort()
even.sort()
lower.sort()
upper.sort()
ans = ''
for char in lower: ans += char
for char in upper: ans += char 
for num in odd: ans += num 
for num in even: ans += num 
print(ans)
