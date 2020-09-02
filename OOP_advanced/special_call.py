class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is: %s.' % self.name)


s = Student('Micheal')
s()

print(callable(Student))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
#  通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
