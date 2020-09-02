from functools import reduce

def add(x, y):
    return x + y
print(reduce(add, [x for x in range(10)]))

def fn(x, y):
    return x*10 + y
print(reduce(fn, [x for x in range(10)]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2num, '13579')))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    return reduce(fn, map(char2num, s))
print(str2int('13579'))

def prod(L):
    def product(x, y):
        return x * y
    return reduce(product, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    s = s.split('.')
    s1 = reduce(fn, map(char2num, s[0]))
    s2 = reduce(fn, map(char2num, s[1]))
    return s1 + s2/10**len(s[1])

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
