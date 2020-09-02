std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

class Student(object):
    def __init__(self, name, score, gender):
        self.name = name
        self.score = score
        self.__gender = gender
    def print_score(self):
        print('%s:%s' % (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender == 'male':
            self.__gender = gender
        elif gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('Invalid gender input!')


michael = Student('Michael', 59, 'male')
bob = Student('Bob', 81, 'male')
michael.print_score()
bob.print_score()
lisa = Student('Lisa', 99, 'female')
bart = Student('Bart', 59, 'male')
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
