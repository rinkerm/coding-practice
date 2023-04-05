cube = lambda x: x**3
def fibonacci_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_r(n-1) + fibonacci_r(n-2)
def fibonacci(n):
    fibs = []
    for i in range(0,n):
        fibs.append(fibonacci_r(i))
    return fibs
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
