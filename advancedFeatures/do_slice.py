L = []
n = 1
while n <= 99:
    L.append(n)
    n += 2
print(L)

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[:-2])
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L)
print(L[:10])
print(L[:-10])
print(L[10:20])
print(L[:10:2])
print(L[::5])
print(L[:])

T = (1,2,3,4)
print(T[:3])

S = 'HELLO, WORLD!'
print(S[:3])

def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s

if trim('hello  ') != 'hello':
    print('fail1!')
elif trim('  hello') != 'hello':
    print('fail2!')
elif trim('  hello  ') != 'hello':
    print('fail3!')
elif trim('  hello  world  ') != 'hello  world':
    print('fail4!')
elif trim('') != '':
    print('fail5!')
elif trim('    ') != '':
    print('fail6!')
else:
    print('success!')
