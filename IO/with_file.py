f = open('test.txt', 'r')
print(f.name)
line = f.read()
print('%s' % line)
f.close()

try:
    f = open('test.txt', 'r')
    print(line)
finally:
    if f:
        f.close()

with open('test.txt', 'r') as f:
    print(line)


'''
with语法和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
'''

f1 = open('test.txt', 'r')
for line in f1.readlines():
    print(line.strip())
f1.close()


with open('test.txt', 'w') as f:
    f.write('Hello, world!')



