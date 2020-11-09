import sys

line = sys.stdin.readline().strip().split(" ")
num1 = int(line[0][::-1])
num2 = int(line[1][::-1])
print(max(num1,num2))
