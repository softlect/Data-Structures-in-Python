def fibonacci(n):
    t0 = 0
    t1 = 1
    sum = 0
    if n <= 1:
        return n
    for i in range(2,n+1):
        sum = t0 + t1
        t0 = t1
        t1 = sum
    return sum


num = input('Enter Number: ')
n = int(num)
for i in range(0, n):
    print(fibonacci(i), end=' ')


