def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(5))

def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact1(5))

def Fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return Fib(n - 1) + Fib(n - 2)
print(Fib(11))


def move(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        move(n-1, a, c, b)
        print(a, '--->', c)
        move(n-1, b, a, c)
move(3,'A','B','C')
