names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print(name)

sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print(sum1)

sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print(sum2)

#  Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello, " + name + "!")

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

