import os
print(os.name)
'''如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。'''

'''注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。'''

#  在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)

#  要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

#  查看当前目录的绝对路径:
print(os.path.abspath('.'))
#  在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('E:\Self Learning\IO', 'testdir'))
#  然后创建一个目录:
os.mkdir('E:\Self Learning\IO\_testdir')
# 删掉一个目录:
os.rmdir('E:\Self Learning\IO\_testdir')
#  要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
#  这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('E:\Self Learning\IO\_testdir'))
#  新建名为os_test的文本文档:
with open('os_test.txt', 'a+') as f:
    f.write('Hello, world!')
#  对文件重命名:
os.rename('os_test.txt', 'os_test.py')
#  删掉文件:
os.remove('os_test.py')
#  列出当前目录下的所有目录:
print([x for x in os.listdir('.') if os.path.isdir(x)])
#  列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

