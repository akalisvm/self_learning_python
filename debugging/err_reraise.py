def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

'''raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：'''

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')

'''只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。'''
