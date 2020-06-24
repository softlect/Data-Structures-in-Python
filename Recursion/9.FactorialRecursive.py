def factorial_rec(n):
    if n == 0:
        return 1
    return factorial_rec(n - 1) * n


num = input('Enter Number: ')
n = int(num)
print('Factorial: ', factorial_rec(n))

