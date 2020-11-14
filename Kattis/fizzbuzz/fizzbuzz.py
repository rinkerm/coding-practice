import sys
inputs = sys.stdin.readline().strip().split(" ")
x = int(inputs[0])
y = int(inputs[1])
n = int(inputs[2])

for i in range(1,n+1):
	if(i % x == 0 and i % y == 0):
		print("FizzBuzz")
	elif(i % x == 0):
		print("Fizz")
	elif(i % y == 0):
		print("Buzz")
	else:
		print(i)
