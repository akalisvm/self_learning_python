import base64, struct
from collections import namedtuple

'''
准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，
所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
'''

print(struct.pack('>I', 10240099))

'''
pack的第一个参数是处理指令，'>I'的意思是：
>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
'''

print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

'''
根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。
'''

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))

'''
两个字节：
'BM'表示Windows位图，
'BA'表示OS/2位图； 
一个4字节整数：表示位图大小； 
一个4字节整数：保留位，始终为0； 
一个4字节整数：实际图像的偏移量； 
一个4字节整数：Header的字节数； 
一个4字节整数：图像宽度； 
一个4字节整数：图像高度； 
一个2字节整数：始终为1； 
一个2字节整数：颜色数。
'''

'''
(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。
'''

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

BMPHeader = namedtuple('BMPHeader', ('type1', 'type2', 'size', 'keep1', 'offset', 'header_size',
                                     'width', 'height', 'keep2', 'colour_num'))

def bmp_info(data):
    header = BMPHeader._make(struct.unpack('<ccIIIIIIHH', data[:30]))
    if header.type1 == b'B' and header.type2 in [b'M', b'A']:
        return {
            'width': header.width,
            'height': header.height,
            'colour': header.colour_num
        }
    raise TypeError('This is not bmp type!')


bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['colour'] == 16
print('ok')
