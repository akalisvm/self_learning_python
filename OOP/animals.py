class Animal(object):
    def run(self):
        print('The animal is running...')


class Dog(Animal):
    def run(self):
        print('The dog is running...')
    def eat(self):
        print('The dog is eating...')

class Cat(Animal):
    def run(self):
        print('The cat is running...')
    def eat(self):
        print('The cat is eating...')

class Tortoise(Animal):
    def run(self):
        print('The tortoise is running slowly...')

class Timer(object):
    def run(self):
        print('start...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
run_twice(Timer())
