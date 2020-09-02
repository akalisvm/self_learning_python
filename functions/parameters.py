def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s
print(power(5))
print(power(5, 3))


def enroll(name, gender, age=6, city='Beijing'):
    print('name: ', name)
    print('gender: ', gender)
    print('age: ', age)
    print('city: ', city)
enroll('Sarah', 'F')
enroll('Bob', 'M', '7', 'Tianjin')


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())



def calc(*numbers):
    s = 0
    for n in numbers:
        s = s + n * n
    return s

nums = (1,2,3)
print(calc(*nums))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Micheal', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

def person1(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person2('Jack', 24, job='Engineer')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b', 'c')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


def product(*numbers):
    p = 1
    if len(numbers) == 0:
        raise TypeError('Please input at least 1 number!')
    else:
        for n in numbers:
            p = p * n
        return p

print(product(5,6))
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('fail1')
elif product(5, 6) != 30:
    print('fail2')
elif product(5, 6, 7) != 210:
    print('fail3')
elif product(5, 6, 7, 9) != 1890:
    print('fail4')
else:
    try:
        product()
        print('fail5')
    except TypeError:
        print('success')
