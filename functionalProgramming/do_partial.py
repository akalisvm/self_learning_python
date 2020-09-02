import functools

print(int('12345'))
print(int('12345', base=8))
print(int('12345', base=16))

def my_int2(x, base=2):
    return int(x, base)
print(my_int2('100000'))

int2 = functools.partial(int, base=2)
print(int2('100000'))
