print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())


class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))


class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(getattr(obj, 'y'))  # 获取属性'y'
print(obj.y)  # 获取属性'y'
print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404
print(hasattr(obj, 'power'))  # 有属性'power'吗？
print(getattr(obj, 'power'))  # 获取属性'power'

class Student(object):
    def __init__(self, name):
        self.name = name
s = Student('Bob')  # 'Bob'是实例属性
s.score = 90

class Student(object):
    name = 'Student'  # 'Student'是类属性
s = Student()  # 创建实例s
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)  # 打印类的name属性
s.name = 'Micheal'  # 给实例绑定name属性
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问
del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


