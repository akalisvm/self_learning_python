import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand error')
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-1))


def quadratic(a, b, c):
    t = b * 2 - 4 * a * c
    if t > 0:
        x1 = (-b + math.sqrt(t)) / 2 * a
        x2 = (-b - math.sqrt(t)) / 2 * a
        return x1, x2
    elif t == 0:
        x = -b / 2 * a
        return x
    else:
        return None


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('success')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('fail')
else:
    print('success')
