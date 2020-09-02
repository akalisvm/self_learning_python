print(list(range(1, 11)))
print(list(x * x for x in range(1, 11)))
print(list(x * x for x in range(1,11) if x % 2 == 0))
print(list(m + n for m in 'ABC' for n in 'XYZ'))

d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k + ' = ' + v)

print(list(k + ' = ' + v for k,v in d.items()))

L = ['Hello', 'World', 'IBM', 'Apple']
print(list(s.lower() for s in L))
print(list(x if x % 2 == 0 else -x for x in range(1, 11)))
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
