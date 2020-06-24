def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


num = input('Enter Number: ')
n = int(num)
for i in range(0, n):
    print(fibonacci(i), end=' ')

