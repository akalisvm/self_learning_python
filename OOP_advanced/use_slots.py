from types import MethodType

class Student(object):
    def set_score(self, score):
        self.score = score


s = Student()
s.name = 'Micheal'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


s.set_score(100)
print(s.score)
s2 = Student()
s2.set_score(95)
print(s2.score)


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Micheal'
s.age = 25
print(s.name, ':', s.age)


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 99
print(g.score)
