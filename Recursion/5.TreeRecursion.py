def calculate(n):
    if n > 0:
        calculate(n - 1)
        k = n ** 2
        print(k)
        calculate(n - 1)


calculate(3)
