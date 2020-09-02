from collections.abc import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key1 in d:
    print(key1)

for key2 in d.values():
    print(key2)

for key3 in d.items():
    print(key3)

print(isinstance((1,2,3),Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x, y in [(1,1), (2,4), (3,9)]:
    print(x, y)

def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    else:
        min1 = max1 = L[0]
        for a in L:
            if not isinstance(a, (int, float)):
                raise TypeError('Invalid type input!')
            if a < min1:
                min1 = a
            elif a > max1:
                max1 = a
    return min1, max1

L = [1,2,3]
print(findMinAndMax(L))

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
