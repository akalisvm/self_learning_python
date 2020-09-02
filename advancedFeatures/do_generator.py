L = [x*x for x in range(10)]
print(L)

g = (x*x for x in range(10))
for n in g:
    print(n)

def fibonacci1(max1):
    n1, a, b = 0, 0, 1
    while n1 < max1:
        print(b)
        a, b = b, a+b
        n1 += 1
    return 'done'
fibonacci1(6)

def fibonacci2(max2):
    n2, a, b = 0, 0, 1
    while n2 < max2:
        yield b
        a, b = b, a+b
        n2 += 1
    return 'done!'
for n in fibonacci2(6):
    print(n)

f = fibonacci2(6)
while True:
    try:
        x = next(f)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]
    return 'done'
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
