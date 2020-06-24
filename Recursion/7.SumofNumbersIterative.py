def sum_itr(n):
    total = 0
    i = 1
    while i <= n:
        total = total + i
        i = i + 1
    return total


def sum_itr1(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total


num = input('Enter Number: ')
n = int(num)
print(sum_itr1(n))
