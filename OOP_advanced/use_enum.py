from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(1))
print(day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '->', member)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender, Gender):  # gender为枚举成员
            self.gender = gender
        elif isinstance(gender, str):   # gender为枚举成员的名称
            if gender.capitalize() in Gender.__members__.keys():  # Enum的特殊属性__members__是一个将名称映射到枚举成员的字典
                self.gender = Gender[gender.capitalize()]
            else:
                raise ValueError('%s is not a valid gender' % gender)
        elif isinstance(gender, int):  # gender为枚举成员的值
            if gender in Gender.value2member_map_:  # Enum的属性_value2member_map_是包含所有枚举成员的值的列表
                self.gender = Gender(gender)
            else:
                raise ValueError('%s is not a valid gender' % gender)
        else:
            raise ValueError('%s is not a valid gender' % gender)

alan = Student('Alan', 0)
bart = Student('Bart', Gender.Male)
cathy = Student('Cathy', 'female')
for i in [alan, bart, cathy]:
    print(i.gender)

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

