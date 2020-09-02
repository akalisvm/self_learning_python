"""XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。"""

'''
DOM vs SAX
操作XML有两种方法：DOM和SAX。
DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
正常情况下，优先考虑SAX，因为DOM实在太占内存。
在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
举个例子，当SAX解析器读到一个节点时：
<a href="/">python</a>
会产生3个事件：
start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时。
'''

#  用代码实验一下：
# 利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器
# 解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
# 而事件处理器则负责对事件作出响应，对传递的XML数据进行处理
from xml.parsers.expat import ParserCreate   # 引入xml解析模块
from urllib import request  # 引入URL请求模块

class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))  # name表示节点名称，attrs表示节点属性（字典）

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)  # text表示节点数据


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

'''
需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。
除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：
'''

L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(r'</root>')
xml = ''.join(L)
print('\n' + xml)

'''
练习：
请利用SAX编写程序解析XML格式的天气预报，获取天气预报：
功能：获取北京市所有地区的当天天气预报信息——（地区名：｛当日天气状态：’‘，最高温度：’‘，最低温度｝）
'''
# -*- coding:utf-8 -*-

class WeatherSaxHandler(object):  # 定义一个天气事件处理器

    weather = {'city': 1, 'cityname': [], 'forecast': []}  # 初始化城市city和预报信息forecast

    def start_element(self, name, attrs):  # 定义开始标签处理事件
        if name == 'beijing':
            self.weather['city'] = '北京'
        if name == 'city':  # 获取location信息
            self.weather['cityname'].append(attrs['cityname'])  # 获取地区名
            # 获取forecast信息
            self.weather['forecast'].append({
                'state': attrs['stateDetailed'],
                'high': attrs['tem2'],
                'low': attrs['tem1']
            })


def parseXml(xml_str):  # 定义xml解析器

    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)  # 解析xml文本
    print('City:' + handler.weather['city'])
    for (x, y) in zip(handler.weather['cityname'], handler.weather['forecast']):  # 打印天气信息
        print('Region:' + x)
        print(y)

    return handler.weather

URL = 'http://flash.weather.com.cn/wmaps/xml/beijing.xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))

