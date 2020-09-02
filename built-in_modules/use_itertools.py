"""
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"""

import itertools
#  count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
naturals = itertools.count(1)
counter1 = 0
print('itertools.count():')
for n in naturals:
    print(n, end=' ')
    counter1 += 1
    if counter1 == 10:
        break

#  cycle()会把传入的一个序列无限重复下去, 同样停不下来。
print('\nitertools.cycle():')
counter2 = 0
cs = itertools.cycle('ABC')
for c in cs:
    counter2 += 1
    print(c, end=' ')
    if counter2 == 10:
        break

#  repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
print('\nitertools.repeat():')
ns = itertools.repeat('A', 3)
for n in ns:
    print(n, end=' ')

'''
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
'''

#  无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
print('\nitertools.takewhile():')
naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, naturals)
print(list(ns))

#  chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
print('itertools.chain():')
for c in itertools.chain('ABC', 'XYZ'):
    print(c, end=' ')

#  groupby()把迭代器中相邻的重复元素挑出来放在一起
print('\nitertools.groupby():')
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

'''
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
'''
print('itertools.groupby().upper():')
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

def pi(N):
    """ 计算pi的值 """
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    os = itertools.takewhile(lambda x: x <= 2*N-1, odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    tmp = map(lambda x: 4/x if x % 4 == 1 else -4/x, os)
    # step 4: 求和:
    return sum(tmp)

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
