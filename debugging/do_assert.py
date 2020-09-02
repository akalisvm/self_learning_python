def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

# main()

'''用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。'''

'''凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：'''
def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo1('0')

main()
