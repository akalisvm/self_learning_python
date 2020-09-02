print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def build(x, y):
    return lambda: x * x + y * y

def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))
print(L1)

L2 = list(filter(lambda x: x % 2 == 1, range(1,20)))
print(L2)
