import types

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
print('')

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))
print(isinstance(d,Dog) and isinstance(d,Animal))
print('')

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print(isinstance([1,2,3], (list, tuple)))
print(isinstance((1,2,3), (list, tuple)))

#    总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

