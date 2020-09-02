def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [x for x in range(10)])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', 'B', '', None, 'C', '    '])))

def odd_iter():
    n1 = 1
    while True:
        n1 = n1 + 2
        yield n1

def not_divisible(n2):
    return lambda x:x % n2 > 0

def prime():
    yield 2
    it = odd_iter()
    while True:
        n3 = next(it)
        yield n3
        it = filter(not_divisible(n3), it)

for n in prime():
    if n < 1000:
        print(n)
    else:
        break

def is_palindrome(num):
    if not isinstance(num, int):
        raise TypeError('Invalid type!')
    if num == int(str(num)[::-1]):
        return True
print(is_palindrome(121))

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')



