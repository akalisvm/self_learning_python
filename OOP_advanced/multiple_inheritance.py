class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Mammal):
    pass


class Runnable(object):
    def run(self):
        print('This animal is running...')


class Flyable(object):
    def fly(self):
        print('This animal is flying...')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Runnable):
    pass

#  MixIn
