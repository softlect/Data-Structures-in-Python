def fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (x, y) = fibonacci(n-1)
        return (x+y, x)


num = input('Enter Number: ')
n = int(num)
for i in range(0, n):
    print(fibonacci(i), end=' ')

